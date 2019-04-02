package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"sync"
	"time"
)

func f(port string) {

	//ip := os.Args[1]
	//port := os.Args[2]
	ip := "10.102.2.10"
	fmt.Println(ip)
	fmt.Println(port)
	netstring := ip + ":" + port
	fmt.Println(netstring)

	conn, err := net.Dial("udp", netstring)
	if err != nil {
		fmt.Println(err)
	}

	i := 1
	count := 0
	for i == 1 {
		//conn.SetSourcePort("7")
		conn.Write([]byte("pew pew pew pew pew pew pew pew pew pew"))
		defer conn.Close()
		conn.SetReadDeadline(time.Now()) //.Add(1 * time.Second))
		ioutil.ReadAll(conn)
		count += 1
		fmt.Println("pew")
		fmt.Println(count)
	}

}

func main() {
	var wg sync.WaitGroup
	wg.Add(1)
	go f("80")
	go f("80")
	go f("80")
	f("80")
	wg.Wait()
}
