package chat

import (
	"log"

	"golang.org/x/net/context"
)

type Server struct {
}

func (s *Server) SayBonjour(ctx context.Context, mess *Mess) (*Mess, error) {

	// Mess
	log.Printf("Recived the message :  %s", mess.Body)
	return &Mess{Body: "Sending de rien viens de Service "}, nil

}

// gan shall def. def. def.
//
