package main

import "fmt"

func main() {
	// Like C program, need 3 args at time
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	// Do the inverse map by for loop
	fmt.Println("[Jason]: Do the inverse map by for loop")

	// Initial
	fmt.Println("         Initial one map:")
	my_map := make(map[string]int)
	my_map["Father_Age"] = 62
	my_map["MomMOm_Age"] = 57
	fmt.Println("           ", my_map)

	// Inverse Initial
	inverse_map := make(map[int]string)

	// Get len
	//get_len := len(my_map) //get_len=2
	// C program loop as usual..
	for key, value := range my_map {
		inverse_map[value] = key
	}
	fmt.Println("\n[Jason]: ok.... check this out")
	fmt.Println("          ", inverse_map)

}
