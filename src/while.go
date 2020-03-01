package main

import "fmt"

func main(){

	fmt.Println("[Mary]: Basic while loop")
	fmt.Println("----------------------------")
	i := 0
	for i < 6{
		fmt.Println(i)
		i++
	}
	fmt.Println("----------------------------\n")
	

	fmt.Println("[Mary]: Loop with index, value , like python list")
	fmt.Println("------------------------------------------------------")
	my_list := make([]string,0)
	my_list = append(my_list,"a")
	my_list = append(my_list,"b")
	my_list = append(my_list,"c")
	for index, value := range my_list{
		fmt.Println("Index:    ",index, "    Value:  ",value)
	}
	fmt.Println("------------------------------------------------------\n")




}