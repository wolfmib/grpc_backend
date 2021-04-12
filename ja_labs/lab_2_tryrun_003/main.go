package main

//grpc
import (
	"github.com/wolfmib/ja_labs/lab_2_tryrun_003/chat"
	"google.golang.org/grpc"
	"log"
	"net"
)

func main() {

	// server listning port

	lis, err := net.Listen("tcp", ":9000")
	if err != nil {
		log.Fatalf("open lis port 9000 fail:  %v", err)
	}

	// grpc init
	grpcServer := grpc.NewServer()
	s := chat.Server{}

	chat.RegisterChatServiceServer(grpcServer, &s)

	// serve
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("Serve fail:  %v", err)
	}

}
