package main

import "fmt"

func main() {

	// It's like python dict (key: value)
	my_python_dict := make(map[string]int)

	// Add some key, value
	my_python_dict["Key_1"] = 5
	my_python_dict["Key_2"] = 2
	my_python_dict["Key_3"] = 0
	my_python_dict["Key_Wrong"] = 999

	fmt.Println(my_python_dict)
	fmt.Println("\nOps! .. Je ne veut  pas la 'key_wrong' plus\n")
	delete(my_python_dict, "Key_Wrong")
	fmt.Println(my_python_dict)

	// Bien sure, tu peux utiliser la 'inverse_dict' (value, key)
	fmt.Println("\n\n------------Using Inverse (Value,Key)---------")
	my_inverse_python_dict := make(map[int]string)

	my_inverse_python_dict[5] = "Key_1"
	my_inverse_python_dict[2] = "Key_2"
	my_inverse_python_dict[0] = "Key_3"
	fmt.Println(my_inverse_python_dict)

}
