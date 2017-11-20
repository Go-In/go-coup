package main

import (
	"fmt"
	"math/rand"
	"time"

	"github.com/go-redis/redis"
)

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

func main() {
	handleRequests()
}
