package main

import "net/http"

func main() {
	ip := "http://149.28.105.154"
	resp, err := http.Get(ip)
	if err != nil {
		print("error")
	}
	print(resp)

}
