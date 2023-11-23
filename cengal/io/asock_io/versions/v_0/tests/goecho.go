// Taken from https://gist.github.com/paulsmith/775764#file-echo-go

package main

import (
	"fmt"
	"net"
	"strconv"
)

const PORT = 18495

func main() {
	fmt.Printf("Started\n")
	server, err := net.Listen("tcp", ":"+strconv.Itoa(PORT))
	if server == nil {
		panic("couldn't start listening: " + err.Error())
	}
	i := 0
	for {
		client, err := server.Accept()
		if client == nil {
			fmt.Printf("couldn't accept: " + err.Error())
			continue
		}
		i++
		fmt.Printf("%d: %v <-> %v\n", i, client.LocalAddr(), client.RemoteAddr())
		go handleConn(client)
	}
}

//func handleConn(client net.Conn) {
//	// USELES RAW COPYLESS (ORIGINAL VERSION)
//    defer client.Close()
//	buf := make([]byte, 102400)
//	for {
//		reqLen, err := client.Read(buf)
//		if err != nil {
//			break
//		}
//		if reqLen > 0 {
//			client.Write(buf[:reqLen])
//		}
//	}
//}

//func handleConn(client net.Conn) {
//	// COPY FROM BUFF
//    defer client.Close()
//	buf := make([]byte, 102400)
//	for {
//		reqLen, err := client.Read(buf)
//    		resultBuf := make([]byte, reqLen)
//		copy(resultBuf, buf)
//		if err != nil {
//			break
//		}
//		if reqLen > 0 {
//			//client.Write(buf[:reqLen])
//			client.Write(resultBuf)
//		}
//	}
//}

func handleConn(client net.Conn) {
	// WITH SLICES
    defer client.Close()
	buf := make([]byte, 1048576)
	for {
		reqLen, err := client.Read(buf)
    		resultBuf := buf[:reqLen]
		buf = buf[reqLen:]
		if len(buf) <= 0 {
			buf = make([]byte, 102400)
		}
		if err != nil {
			break
		}
		if reqLen > 0 {
			//client.Write(buf[:reqLen])
			client.Write(resultBuf)
		}
	}
}
