package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
    // open the file using Open() function from os library
	file, err := os.Open("test.txt")
	if err != nil {
		log.Fatal(err)
	}

	// read the file line by line using a scanner
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		//Print the line
		fmt.Println(scanner.Text())
	}
    // check for the error that occurred during the scanning
    
    if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
    
	// Close the file at the end of the program
	file.Close()
}