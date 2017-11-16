package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/go-redis/redis"
	"github.com/golang/example/stringutil"
)

type Message struct {
	Name string
	Body string
	Time int64
}

func NewClient() {
	client := redis.NewClient(&redis.Options{
		Addr:     "redis:6379",
		Password: "", // no password set
		DB:       0,  // use default DB
	})

	pong, err := client.Ping().Result()
	fmt.Println(pong, err)
	// Output: PONG <nil>
}

func homePage(w http.ResponseWriter, r *http.Request) {
	m := Message{"Alice", "Hello", 1294706395881547000}
	b, _ := json.Marshal(m)

	fmt.Println(r.PostFormValue("a"))

	w.Header().Set("Content-Type", "application/json")

	fmt.Fprintf(w, string(b))
	fmt.Println("get request at root endpoint")
}

func handleRequests() {
	http.HandleFunc("/", homePage)
	log.Fatal(http.ListenAndServe(":8081", nil))
}

func main() {
	NewClient()
	fmt.Println(stringutil.Reverse("HI"))
	handleRequests()
}
