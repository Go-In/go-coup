package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/go-redis/redis"
)

type Message struct {
	Name string
	Body string
	Time int64
}

type Data struct {
	price    string
	currency string
	reuse    string
}

type Payload struct {
	Key string
	// data   Data
	Status string
}

var client *redis.Client

func NewClient() {
	client = redis.NewClient(&redis.Options{
		Addr:     "redis:6379",
		Password: "",
		DB:       14,
	})

	pong, err := client.Ping().Result()
	fmt.Println(pong, err)
}

func homePage(w http.ResponseWriter, r *http.Request) {
	m := Message{"Alice", "Hello", 1294706395881547000}
	b, _ := json.Marshal(m)
	fmt.Println(b)
	fmt.Println(string(b))
	fmt.Println(r.PostFormValue("a"))

	w.Header().Set("Content-Type", "application/json")

	fmt.Fprintf(w, string(b))
	fmt.Println("get request at root endpoint")
}

func save(w http.ResponseWriter, r *http.Request) {
	// cipher, _ := blowfish.NewCipher([]byte("MM"))
	data := Data{r.PostFormValue("price"), r.PostFormValue("currency"), r.PostFormValue("reuse")}
	key := data.currency + "-" + data.price
	// encrypted := make([]byte, 128)
	// fmt.Println(key)
	// cipher.Encrypt(encrypted, []byte(key))
	// fmt.Println(string(encrypted))

	dataToStr, _ := json.Marshal(data)
	err := client.Set(key, string(dataToStr), 0).Err()
	if err != nil {
		panic(err)
	}

	resPayload := Payload{string(key), "OK"}
	res, err := json.Marshal(resPayload)
	fmt.Println(resPayload)
	fmt.Println(res)
	fmt.Println(string(res))

	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, string(res))
}

func handleRequests() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/save", save)
	log.Fatal(http.ListenAndServe(":8081", nil))
}

func main() {
	NewClient()
	fmt.Println("HI")
	handleRequests()
}
