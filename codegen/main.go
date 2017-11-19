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

type Data struct {
	Price    string
	Currency string
	Reuse    string
}

type Payload struct {
	Status string
	Key    string
	Value  Data
}

func init() {
	NewClient()
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
	var m Payload
	m.Status = "OK"
	b, _ := json.Marshal(m)

	w.Header().Set("Content-Type", "application/json")

	fmt.Fprintf(w, string(b))
}

func save(w http.ResponseWriter, r *http.Request) {
	data := Data{r.PostFormValue("price"), r.PostFormValue("currency"), r.PostFormValue("reuse")}
	key := RandStringRunes(13)
	dataToStr, _ := json.Marshal(data)
	err := client.Set(key, string(dataToStr), 0).Err()
	if err != nil {
		panic(err)
	}

	resPayload := Payload{"OK", string(key), data}

	res, err := json.Marshal(resPayload)

	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, string(res))
}

func load(w http.ResponseWriter, r *http.Request) {
	key := r.PostFormValue("key")
	val, err := client.Get(key).Result()
	var data Data

	resPayload := Payload{Key: key}
	if err == redis.Nil {
		resPayload.Status = "NOT_FOUND"
	} else if err != nil {
		resPayload.Status = "INTERNAL_SERVER_ERROR"
	} else {
		error := json.Unmarshal([]byte(val), &data)
		if error != nil {
			panic(error)
		}
		resPayload.Value = data
		resPayload.Status = "OK"

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
	handleRequests()
}
