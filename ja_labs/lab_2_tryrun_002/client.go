package main

import (
	"log"

	"github.com/wolfmib/grpc_backend/ja_labs/lab_2_protobuf_tryrun_002/chat"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

func main() {

	// skip grpc.ClientConn ... init

	// Dial
	conn, err := grpc.Dial(":9000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("conn err: %v", err)
	}
	defer conn.Close()

	c := chat.NewChatServiceClient(conn)

	// message
	sendMess := chat.Mess{
		Body: "hello from client",
	}

	response, err := c.SayBonjour(context.Background(), &sendMess)
	if err != nil {
		log.Fatalf("err when calling %v", err)
	}

	log.Printf("recevois from client:\n  %s\n", response.Body)

}
