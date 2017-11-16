package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/golang/example/stringutil"
)

type Message struct {
	Name string
	Body string
	Time int64
}

func homePage(w http.ResponseWriter, r *http.Request) {
	m := Message{"Alice", "Hello", 1294706395881547000}
	b, _ := json.Marshal(m)

	w.Header().Set("Content-Type", "application/json")

	fmt.Fprintf(w, string(b))
	fmt.Println("get request at root endpoint")
}

func handleRequests() {
	http.HandleFunc("/", homePage)
	log.Fatal(http.ListenAndServe(":8081", nil))
}

func main() {
	fmt.Println(stringutil.Reverse("HI"))
	handleRequests()
}
