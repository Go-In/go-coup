package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/golang/example/stringutil"
)

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "root")
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
