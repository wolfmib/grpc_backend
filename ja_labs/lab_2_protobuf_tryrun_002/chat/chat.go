//implement the method
package chat

//fucking gan lineear

import (
	"log"

	"golang.org/x/net/context"
)

//!!
type Server struct{}

func (s *Server) SayBonjour(ctx context.Context, message *Mess) (*Mess, error) {

	// message
	log.Printf("Recieved the fucking message from the client:  %v", message.Body)

	//returns
	return &Mess{Body: "ganagagan"}, nil

}
