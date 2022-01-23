package main

import (
	"flag"
	"fmt"
	"os"

	 client "gitlab.cs.umd.edu/arasevic/cmsc398Bwinter2022-student/exercises/exercise3"
)

// Default file name
var log = "requestLogs.json"

func main() {
	num_1 := flag.Bool("request", false, "")
	num := flag.Bool("GET", false, "Syntax: -request -GET  -endpoint <endpoint>")
	num1 := flag.Bool("POST", false, "Syntax: -request -POST -endpoint <endpoint> -data <data>")
	num2 := flag.Bool("PUT", false, "Syntax:-request -PUT -endpoint <endpoint> -data <data>")
	num3 := flag.Bool("DELETE", false, "Syntax:-request -DELETE -endpoint <endpoint>")
	num5 := flag.String("data", "", "Syntax:-data <data>")
	num6 := flag.String("endpoint", "", "Syntax: -endpoint <endpoint>")

	num8 := ""
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(),
			"%s cli client. CMSC398B Winter 2022 Exercise 3\n", os.Args[0])
		fmt.Fprintln(flag.CommandLine.Output(), "Usage information:")
		flag.PrintDefaults()
	}
	flag.Parse()

	l := client.List{}

	if *num_1 == true {
		if *num == true {
			fmt.Println(l.Get(*num6, log))
			fmt.Print("JSON FILE OUTPUT : ")
			fmt.Println(l.PrintLogFile((log)))
		}
		if *num1 == true {
			l.Postaux(*num6, *num5, "application/json", log)
			fmt.Print("JSON FILE OUTPUT : ")
			fmt.Println(l.PrintLogFile((log)))
		}
		if *num3 == true {
			l.Delete(*num6, log)
			fmt.Print("JSON FILE OUTPUT : ")
			fmt.Println(l.PrintLogFile((log)))
		}
		if *num2 == true {
			l.Put(*num5, *num6, log)
			fmt.Print("JSON FILE OUTPUT : ")
			fmt.Println(l.PrintLogFile((log)))
		}
		if num5 == nil {
			fmt.Println("Data Not Provided")
		}
		if *num6 == num8 {
			fmt.Println("Endpoint Not Provided")
		}
	} else {
		flag.Usage()
		os.Exit(1)
	}
}
