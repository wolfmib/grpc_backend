package chat

import (
	"golang.org/x/net/context"
	"log"
)

type Server struct{}

func (s *Server) SayBonjour(ctx context.Context, mess *Mess) (*Mess, error) {

	log.Printf("Recv messae viens de Client :    \n %s\n", mess.Body)

	return &Mess{Body: "[Server] Say Bonjour  !! "}, nil

}
