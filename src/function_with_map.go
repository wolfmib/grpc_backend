package main

import "fmt"
// Author: Mary
	// Simple checking.

func mongo_insert_data(INPUT_DATA map[string] string){
	// implement mongo client here
	for key, value := range INPUT_DATA{
		fmt.Print("Insert  key: ",key, "      ,    Insert value:   ", value,"\n")
	}
}


func main(){

	my_data_in_main := make(map[string] string)
	my_data_in_main["firstname"] = "mary"
	my_data_in_main["lastname"] = "cheng"

	mongo_insert_data(my_data_in_main)


}