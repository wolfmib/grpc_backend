package main

import (
	"log"

	"github.com/wolfmib/grpc_backend/ja_labs/lab_2_protobuf/chat"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

func main() {

	//conn
	var conn *grpc.ClientConn

	conn, err := grpc.Dial(":9000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("err when grpc.Dial:   %v", err)
	}

	defer conn.Close()

	//c client
	c := chat.NewChatServiceClient(conn)

	sendMess := chat.Mess{
		Body: "Sedning from the Client",
	}

	// call
	res, err := c.SayBonjour(context.Background(), &sendMess)
	if err != nil {
		log.Fatalf("err when grpc.Dial:   %v", err)
	}

	log.Printf("Response:    %s", res.Body)

}
