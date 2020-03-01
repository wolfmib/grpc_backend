package main

import (
	"errors"
	"fmt"
	"math"
)

func main() {
	fmt.Println("Test: sqrt(2)")
	// [Jean]: Vous pouvez utiliser ce code sur une seule ligne.
	fmt.Println(sqrt(2), "\n")

	fmt.Println("Test: power(3,2)")
	res, _ := power(2, 3)
	fmt.Println(res, "\n")

	fmt.Println("Test: power(10, 3), which will cause error, if 10 > 9, test only ")
	res, err := power(10, 3)
	if err != nil {
		fmt.Println("[Error]:  ", err, "\n")
	} else {
		fmt.Println(res, "\n")
	}

}

// [Jean]: C'est Custom funcion
/*
	math.sqrt
	power(n,number) = [ number ^ n]
*/
func sqrt(n int) float64 {
	return_number := math.Sqrt(2)
	return return_number
}

func power(n int, number float64) (float64, error) {

	if n >= 10 {
		return 0.0, errors.New("[Jean]: System didn't support non-interger n")
	} else {
		var _result float64 = 1
		for i := 0; i < n; i++ {
			_result = _result * number
		}
		return _result, nil
	}
}
