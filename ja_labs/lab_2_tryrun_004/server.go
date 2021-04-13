package main

import (
	"github.com/wolfmib/lab_2_tryrun_004/chat"
	"google.golang.org/grpc"
	"log"
	"net"
)

func main() {

	lis, err := net.Listen("tcp", ":9000")
	if err != nil {
		log.Fatalf("open port fail: %v\n", err)
	}

	grpcServer := grpc.NewServer()
	s := chat.Server{}

	chat.RegisterChatServiceServer(grpcServer, &s)

	//serve
	log.Printf("Commencer .... dans la 9000\n")
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("Serve fail: %v", err)
	}

}
