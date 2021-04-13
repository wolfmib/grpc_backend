package main

import (
	"github.com/wolfmib/lab_2_tryrun_004/chat"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"log"
)

func main() {

	// conn
	conn, err := grpc.Dial(":9000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("fail to make conn for 9000:  %v\n", err)
	}

	defer conn.Close()

	// call la gan
	c := chat.NewChatServiceClient(conn)

	sendMess := chat.Mess{
		Body: "sending greeting from Chat...",
	}

	res, err := c.SayBonjour(context.Background(), &sendMess)
	if err != nil {
		log.Fatalf("Fail to send messager to grpcserver:  %v", err)
	}

	log.Printf("Reve the mess from server:   \n%s\n", res.Body)

}
