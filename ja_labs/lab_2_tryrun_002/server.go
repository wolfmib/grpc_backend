package main

import (
	"log"
	"net"

	"github.com/wolfmib/grpc_backend/ja_labs/lab_2_protobuf_tryrun_002/chat"
	"google.golang.org/grpc"
)

func main() {

	// listening port
	lis, err := net.Listen("tcp", ":9000")
	if err != nil {
		log.Fatalf("open 9000 port fial  %v", lis)
	}

	// grpc server init
	s := chat.Server{}

	grpcServer := grpc.NewServer()

	chat.RegisterChatServiceServer(grpcServer, &s)

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("grpc Serve fail:  %v", err)
	}

}

/*

 syntax    ;
 package ;

 option go_package = "oooo" ;

 message OOO{
	 string ooo = 1;
 }


 service OOService {
	 rpc SayHello(OOO) returns OOO{}
 }


 // remember the
 s := chat.Server{} , it's {} not ()
 // then the client lol !!!


--------
client.go
----

pckage main

log
golang.org/x/net/context
google.golang.org/grpc
github/ooooo/chat


var conn *grpc.ClientConn // maybe, you don't need this..
conn , err := grpc.Dial(":9000",grpc.withinsecure)
err.....


defer conn.Close()

sendMess := chat.Mess{
	Body: "Gan",
}

c := chat.NewChastServiceClient(conn)
response , err := c.SayBonjour(context.Background(),&sendMess)
if err ....


print(response.Body )

// score 70
// time spend :   fucking 90 mins.... too long
// try lab try_run_3 , get 20mins is your goal !




*/
