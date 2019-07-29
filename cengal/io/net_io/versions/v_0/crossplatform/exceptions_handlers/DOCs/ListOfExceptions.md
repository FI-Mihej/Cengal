# Exceptions handlers

* 344 - add_gate - add passive connection
    * Exceptions:
        * create socket & setblocking(0)
        * bind
        * listen
    * Finally:
        * return address of connection to be added to a set_of_gate_addresses. (AF_UNIX is available only on UNIX OS). This method should be placed in the connection. Браться он тоже должен из соединения.

* 844 - _connect_to_super_server - add active_connected socket:
    * Exceptions:
        * create socket
        * connect
        * getaddrinfo & gethostbyaddr. Unix / NT. Not available for AF_UNIX).

* 999 - _connect_to_super_server - add active_accepted socket:
    * Exceptions:
        * accept
        * getaddrinfo & gethostbyaddr. Unix / NT. Not available for AF_UNIX).

* 1242 - _read_data_from_already_connected_socket__shell - read data from socket
    * Exceptions:
        * recv_into / recv. Algorithm per connection. Unix / NT.

* 1515 - _write_data_to_socket - write data to socket
    * Exceptions:
        * send. Algorithm per connection. Unix / NT.

# API suggestions

* flag "auto unlink AF_UNIX socket if already exist". Default: False. See: 2097, 2108. on asock_io_core.py

