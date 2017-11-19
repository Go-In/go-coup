package main

import (
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/go-redis/redis"
)

type Message struct {
	Name string
	Body string
	Time int64
}

type Data struct {
	Price    string
	Currency string
	Reuse    string
}

type Payload struct {
	Key    string
	Value  Data
	Status string
}

func init() {
	rand.Seed(time.Now().UnixNano())
}

var letterRunes = []rune("01234567890ABCDEF")
var client *redis.Client

func RandStringRunes(n int) string {
	b := make([]rune, n)
	for i := range b {
		b[i] = letterRunes[rand.Intn(len(letterRunes))]
	}
	return string(b)
}

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
	data := Data{r.PostFormValue("price"), r.PostFormValue("currency"), r.PostFormValue("reuse")}
	key := RandStringRunes(13)
	fmt.Printf(key)
	dataToStr, _ := json.Marshal(data)
	err := client.Set(key, string(dataToStr), 0).Err()
	if err != nil {
		panic(err)
	}

	resPayload := Payload{string(key), data, "OK"}
	res, err := json.Marshal(resPayload)
	fmt.Println(resPayload)
	fmt.Println(res)
	fmt.Println(string(res))

	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, string(res))
}

func load(w http.ResponseWriter, r *http.Request) {
	key := r.PostFormValue("key")
	val, err := client.Get(key).Result()
	var data Data

	resPayload := Payload{Key: key}
	if err == redis.Nil {
		resPayload.Status = "notfound"
	} else if err != nil {
		resPayload.Status = "servererror"
	} else {
		error := json.Unmarshal([]byte(val), &data)
		if error != nil {
			fmt.Println("error")
			panic(error)
		}
		resPayload.Value = data
		resPayload.Status = "ok"

	}
	res, err := json.Marshal(resPayload)
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, string(res))

}

func handleRequests() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/save", save)
	http.HandleFunc("/load", load)
	fmt.Println("Listen and serve on PORT 8081")
	log.Fatal(http.ListenAndServe(":8081", nil))
}

func main() {
	NewClient()
	handleRequests()
}
