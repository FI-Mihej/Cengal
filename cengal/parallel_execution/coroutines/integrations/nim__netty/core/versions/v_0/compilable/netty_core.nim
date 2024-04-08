# mymodule.nim - file name should match the module name you're going to import from python
import nimpy
import compile_time_py_definitions
import netty
import std/tables
import sequtils
import strutils
import std/[times, os]


func toBytes*(s: string): seq[byte] =
  @(s.toOpenArrayByte(0, s.high))


type
  PyAddress* = object
    ## A host/port of the client.
    host*: string
    port*: uint16

  PyConnectionStats* = object
    inFlight*: int   ## How many bytes are currently in flight.
    inQueue*: int    ## How many bytes are currently waiting to be sent.
    saturated*: bool ## If this conn cannot send until it receives acks.

  PyConnection* = object
    id*: uint32
    reactorId*: uint32
    address*: PyAddress
    stats*: PyConnectionStats
    lastActiveTime*: float64
  
  PyReactor* = object
    id*: uint32
    address*: PyAddress
    maxInFlight*: int                 ## Max bytes in-flight on the socket.
    debug*: DebugConfig

  # ByteMessage = openArray[byte]
  # ByteMessageRef = ref openArray[byte]
  StrMessages = seq[string]
  StrMessagesPerConnection = Table[uint32, StrMessages]
  ByteMessages = seq[seq[byte]]
  # ByteMessages = seq[seq[char]]
  ByteMessagesPerConnection = Table[uint32, ByteMessages]
  TickResult = object
    server_received*: ByteMessagesPerConnection
    client_received*: ByteMessagesPerConnection
    server_new_connections*: seq[PyConnection]
    client_new_connections*: seq[PyConnection]
    server_dead_connections*: seq[PyConnection]
    client_dead_connections*: seq[PyConnection]
    server_failed_to_send_connections*: seq[uint32]
    client_failed_to_send_connections*: seq[uint32]

var
  servers: Table[uint32, Reactor] = initTable[uint32, Reactor]()
  server_connections: Table[uint32, Connection] = initTable[uint32, Connection]()
  clients: Table[uint32, Reactor] = initTable[uint32, Reactor]()
  client_connections: Table[uint32, Connection] = initTable[uint32, Connection]()
  # servers_pending_messages: StrMessagesPerConnection = initTable[uint32, StrMessages]()
  # servers_received_messages: StrMessagesPerConnection = initTable[uint32, StrMessages]()
  # clients_pending_messages: StrMessagesPerConnection = initTable[uint32, StrMessages]()
  # clients_received_messages: StrMessagesPerConnection = initTable[uint32, StrMessages]()


func toPy(address: Address): PyAddress =
  return PyAddress(host: address.host, port: uint16(address.port))


func fromPy(address: PyAddress): Address =
  return Address(host: address.host, port: Port(address.port))


func toPy(stats: ConnectionStats): PyConnectionStats =
  return PyConnectionStats(inFlight: stats.inFlight, inQueue: stats.inQueue, saturated: stats.saturated)


func fromPy(stats: PyConnectionStats): ConnectionStats =
  return ConnectionStats(inFlight: stats.inFlight, inQueue: stats.inQueue, saturated: stats.saturated)


func toPy(connection: Connection): PyConnection =
  return PyConnection(id: connection.id, reactorId: connection.reactorId, address: toPy(connection.address), stats: toPy(connection.stats), lastActiveTime: connection.lastActiveTime)


func toPy(reactor: Reactor): PyReactor =
  return PyReactor(id: reactor.id, address: toPy(reactor.address), maxInFlight: reactor.maxInFlight, debug: reactor.debug)


proc serve(addr_list: seq[PyAddress]): seq[PyReactor] {.exportpy.} =
  var
    new_servers: seq[PyReactor] = @[]
  
  for address in addr_list:
    var server: Reactor = newReactor(address.fromPy())
    servers[server.id] = server
    new_servers.add(server.toPy())
  
  return new_servers


proc clientImpl(): Reactor =
  var client_obj: Reactor
  if 0 == clients.len:
    client_obj = newReactor()
    clients[client_obj.id] = client_obj
  else:
    for client_id, client_reactor in clients:
      client_obj = client_reactor
      break
  
  return client_obj


proc client(): PyReactor {.exportpy.} =
  return clientImpl().toPy()


proc connect(addr_list: seq[PyAddress]): seq[PyConnection] {.exportpy.} =
  var
    new_connections: seq[PyConnection] = @[]
  
  var client: Reactor = clientImpl()
  for address in addr_list:
    var connection: Connection = client.connect(address.fromPy())
    client_connections[connection.id] = connection
    new_connections.add(connection.toPy())
  
  return new_connections


proc server_disconnect(reactorId: uint32; connectionId: uint32): bool {.exportpy.} =
  if reactorId notin servers:
    return false

  if connectionId notin server_connections:
    return false

  let server = servers[reactorId]
  let connection = server_connections[connectionId]
  disconnect(server, connection)
  return true


proc client_disconnect(reactorId: uint32; connectionId: uint32): bool {.exportpy.} =
  if reactorId notin clients:
    return false

  if connectionId notin client_connections:
    return false

  let client = clients[reactorId]
  let connection = client_connections[connectionId]
  disconnect(client, connection)
  return true


proc punch_through(address: PyAddress) {.exportpy.} =
  clientImpl().punchThrough(address.fromPy())


proc tick(
  server_send: StrMessagesPerConnection; 
  client_send: StrMessagesPerConnection; 
  ): TickResult {.exportpy.} =
  # let time = cpuTime()
  var tick_result: TickResult
  # server
  for server_id, server in servers:
    # let time0 = cpuTime()
    server.tick()
    # echo "0 Time taken: ", cpuTime() - time0
    for msg in server.messages:
      let server_msg_data_str = msg.data
      # echo server_msg_data_str
      let server_msg_data_bytes = cast[seq[byte]](server_msg_data_str)
      # let server_msg_data_bytes = server_msg_data_str.toBytes()
      # echo server_msg_data_bytes
      if msg.conn.id notin tick_result.server_received:
        tick_result.server_received[msg.conn.id] = @[]
      
      tick_result.server_received[msg.conn.id].add(server_msg_data_bytes)
    
    for connection in server.newConnections:
      tick_result.server_new_connections.add(connection.toPy())
      server_connections[connection.id] = connection
    
    for connection in server.deadConnections:
      tick_result.server_dead_connections.add(connection.toPy())
      server_connections.del(connection.id)
  
  for server_connection_id, server_send_msg in server_send:
    if server_connection_id in server_connections:
      let server_send_connection = server_connections[server_connection_id]
      let server_send_reactor = servers[server_send_connection.reactorId]
      for server_connection_str_message in server_send_msg:
        server_send_reactor.send(server_send_connection, server_connection_str_message)
    else:
      tick_result.server_failed_to_send_connections.add(server_connection_id)

  for server_id, server in servers:
    # let time1 = cpuTime()
    server.tick()
    # echo "1 Time taken: ", cpuTime() - time1
    for msg in server.messages:
      let server_msg_data_str = msg.data
      let server_msg_data_bytes = cast[seq[byte]](server_msg_data_str)
      # let server_msg_data_bytes = server_msg_data_str.toBytes()
      # echo server_msg_data_bytes
      if msg.conn.id notin tick_result.server_received:
        tick_result.server_received[msg.conn.id] = @[]
      
      tick_result.server_received[msg.conn.id].add(server_msg_data_bytes)
    
    for connection in server.newConnections:
      tick_result.server_new_connections.add(connection.toPy())
      server_connections[connection.id] = connection
    
    for connection in server.deadConnections:
      tick_result.server_dead_connections.add(connection.toPy())
      server_connections.del(connection.id)
  
  # client
  for client_id, client in clients:
    # let time2 = cpuTime()
    client.tick()
    # echo "2 Time taken: ", cpuTime() - time2
    for msg in client.messages:
      let client_msg_data_str = msg.data
      let client_msg_data_bytes = cast[seq[byte]](client_msg_data_str)
      # let client_msg_data_bytes = client_msg_data_str.toBytes()
      # echo client_msg_data_bytes
      if msg.conn.id notin tick_result.client_received:
        tick_result.client_received[msg.conn.id] = @[]
      
      tick_result.client_received[msg.conn.id].add(client_msg_data_bytes)
    
    for connection in client.newConnections:
      tick_result.client_new_connections.add(connection.toPy())
    
    for connection in client.deadConnections:
      tick_result.client_dead_connections.add(connection.toPy())
      client_connections.del(connection.id)
  
  for client_connection_id, client_send_msg in client_send:
    if client_connection_id in client_connections:
      let client_send_connection = client_connections[client_connection_id]
      let client_send_reactor = clients[client_send_connection.reactorId]
      for client_connection_str_message in client_send_msg:
        # echo client_connection_str_message
        client_send_reactor.send(client_send_connection, client_connection_str_message)
    else:
      tick_result.client_failed_to_send_connections.add(client_connection_id)

  for client_id, client in clients:
    # let time3 = cpuTime()
    client.tick()
    # echo "3 Time taken: ", cpuTime() - time3
    for msg in client.messages:
      let client_msg_data_str = msg.data
      let client_msg_data_bytes = cast[seq[byte]](client_msg_data_str)
      # let client_msg_data_bytes = client_msg_data_str.toBytes()
      # echo client_msg_data_bytes
      if msg.conn.id notin tick_result.client_received:
        tick_result.client_received[msg.conn.id] = @[]
      
      tick_result.client_received[msg.conn.id].add(client_msg_data_bytes)
    
    for connection in client.newConnections:
      tick_result.client_new_connections.add(connection.toPy())
    
    for connection in client.deadConnections:
      tick_result.client_dead_connections.add(connection.toPy())
      client_connections.del(connection.id)
  
  # echo "Time taken: ", cpuTime() - time
  return tick_result
