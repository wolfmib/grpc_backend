package chat

import (
	"golang.org/x/net/context"
	"log"
)

type Server struct{}

func (s *Server) SayBonjour(ctx context.Context, mess *Mess) (*Mess, error) {

	// body
	log.Printf("Recv the message from Client the body is  %s\n", mess.Body)

	// return la
	return &Mess{Body: "Hello from the server side , it's run: 004 lo .."}, nil
}
