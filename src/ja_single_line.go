package main

import "fmt"

func main() {

	number := 30
	// Type
	fmt.Printf("number type is %T\n", number)

	var bl bool
	fmt.Printf("bl type is %T\n", bl)

	// Hello World
	fmt.Println("Hello World!", number)

	//
	fmt.Printf("Number x:   %x\n", 16)

	// Let's make slice for one list
	// case: H1 4:  SingleRow := []string{"H1", "H1", "H1", "W1", "L1"}
	// case: H1 4:  SingleRow := []string{"H1", "H1", "H1", "H1", "L1"}
	// case: H1 4 > wild 2: SingleRow := []string{"W1", "W1", "H1", "H1", "L1"}
	// case: H1 3 > wild 2: SingleRow := []string{"W1", "W1", "H1", "S1", "L1"}
	// case: H2 3 < wild 2: SingleRow := []string{"W1", "W1", "H2", "S1", "L1"}
	SingleRow := []string{"W1", "W1", "L2", "L2", "S1"}

	fmt.Printf("single_row: %s\n", SingleRow)

	// Loop Slice
	for i, value := range SingleRow {

		fmt.Printf("%d:   %s\n", i, value)

	}

	// Let's use map to make pay_table
	//make list with slice
	SymbolList := []string{"L1", "L2", "L3", "H1", "H2", "H3", "S1", "W1"}

	//initial paytable with map
	PayTable := map[string]map[int]int{
		"H1": map[int]int{
			2: 0,
			3: 70,
			4: 200,
			5: 500,
		},
		"H2": map[int]int{
			2: 0,
			3: 50,
			4: 200,
			5: 500,
		},

		"L1": map[int]int{
			2: 0,
			3: 25,
			4: 55,
			5: 105,
		},
		"L2": map[int]int{
			2: 0,
			3: 20,
			4: 50,
			5: 100,
		},
		"W1": map[int]int{
			2: 60,
			3: 210,
			4: 600,
			5: 1000,
		},
	}

	/*
		W1, W1, W1, W1 , count_win_line = 4 , loop obj H1, check if exist at least H1
		W1, H1, W1, H1 , count_win_line = 4 , loop obj H1
	*/

	// Assign single value
	fmt.Println(PayTable)

	fmt.Println(PayTable["W1"][5])

	// Check win_gain first
	countWinWild := 0
	for _, eachSinbleRowSymbol := range SingleRow {
		if eachSinbleRowSymbol == "W1" {
			countWinWild++
		} else {
			break
		}
	}

	currWildGain := PayTable["W1"][countWinWild]

	// Checking loop
	currObjGain := 0
	countWinObj := 0
	for _, eachSymbol := range SymbolList {
		fmt.Println("Checking symbol:  ", eachSymbol)

		countWinObj = 0
		if eachSymbol != "W1" {

			for _, eachSingleRunSymbol := range SingleRow {
				if eachSingleRunSymbol == eachSymbol || eachSingleRunSymbol == "W1" {
					countWinObj++
				} else {
					break
				}
			}
			// show each result
			if countWinObj > countWinWild {
				// Display info
				fmt.Println(SingleRow)
				fmt.Println(PayTable)

				currObjGain = PayTable[eachSymbol][countWinObj]

				// Get win_gain, Save time: just break
				break
			}
		}
	}

	// obj gain > wild gain
	if currObjGain > currWildGain {

		fmt.Printf("obj_win_gain >  wild_gain:    obj_winLine:    %2d,    with gain   %d\n\n", countWinObj, currObjGain)
	} else {
		fmt.Printf("obj_win_gain <=  wild_gain:   wild_winLine:   %2d,    with gain   %d\n\n", countWinWild, currWildGain)
	}

}
