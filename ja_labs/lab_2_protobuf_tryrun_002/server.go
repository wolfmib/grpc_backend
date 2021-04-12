package main

import (
	"log"
	"net"

	"github.com/wolfmib/grpc_backend/ja_labs/lab_2_protobuf/chat"
	"google.golang.org/grpc"
)

func main() {

	// Port
	lis, err := net.Listen("tcp", ":9000")
	if err != nil {
		log.Fatalf("can't open the fucking port %v", err)
	}

	// Pert to Server
	grpcServer := grpc.NewServer()

	s := chat.Server{}

	chat.RegisterChatServiceServer(grpcServer, &s)

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("Can't binding the server to the fucking port!!")
	}

}
