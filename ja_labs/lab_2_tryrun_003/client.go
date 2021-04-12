package main

import (
	"github.com/wolfmib/ja_labs/lab_2_tryrun_003/chat"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"log"
)

func main() {
	// conn
	conn, err := grpc.Dial(":9000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Dial fail:  %v", err)
	}

	// creer chat client
	c := chat.NewChatServiceClient(conn)

	//
	sendMess := chat.Mess{
		Body: "hihuihuihuhuhihiuhiuhui",
	}

	// call rpc:
	res, err := c.SayBonjour(context.Background(), &sendMess)
	if err != nil {
		log.Fatalf("SayBonjour fail dans la Client:  %v", err)
	}

	log.Printf("Received the message from server:    %s\n", res.Body)

}
