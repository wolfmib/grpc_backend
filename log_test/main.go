package main
import "log"
import logrus "github.com/sirupsen/logrus"

func main(){
	log.Println("[Jean]: I am backend.")
	log.Println("[Jason]: I am api-layer")
	log.Println("[Mary]: I am frontend.")

	log.Println("-------logrus-----------")
	logrus.Info("[Jean]: I am backend.")
	logrus.Warn("[Jason]: I am api-layer")
	logrus.Fatal("[Mary]: I am frontend.")
	

}
