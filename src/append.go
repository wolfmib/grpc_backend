package main

import "fmt"

func main() {

	similar_to_python_list := make([]int, 5)
	fmt.Println(similar_to_python_list)
	similar_to_python_list = append(similar_to_python_list, 5)
	similar_to_python_list = append(similar_to_python_list, 2)
	similar_to_python_list = append(similar_to_python_list, 0)
	fmt.Println(similar_to_python_list)

	fmt.Println("\n\n\nBetter suggesed is to initial  with nothing , then append after")
	initial_zero_list := make([]int, 0)
	fmt.Println(initial_zero_list)
	initial_zero_list = append(initial_zero_list, 333)
	fmt.Println(initial_zero_list)

}
