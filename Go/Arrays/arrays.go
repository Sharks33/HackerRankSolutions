package main

import (
	"fmt"
)

// Complete the reverseArray function below.
func reverseArray(a []int32) []int32 {
	for i := 0; i < len(a)/2; i++ {
		j := len(a) - i - 1
		a[i], a[j] = a[j], a[i]
	}
	return a
}

func main() {
	arr := []int32{1, 2, 3, 4}
	fmt.Println(reverseArray(arr))

	// 	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	// 	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	// 	checkError(err)

	// 	defer stdout.Close()

	// 	writer := bufio.NewWriterSize(stdout, 1024*1024)

	// 	arrCount, err := strconv.ParseInt(readLine(reader), 10, 64)
	// 	checkError(err)

	// 	arrTemp := strings.Split(readLine(reader), " ")

	// 	var arr []int32

	// 	for i := 0; i < int(arrCount); i++ {
	// 		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
	// 		checkError(err)
	// 		arrItem := int32(arrItemTemp)
	// 		arr = append(arr, arrItem)
	// 	}

	// 	res := reverseArray(arr)

	// 	for i, resItem := range res {
	// 		fmt.Fprintf(writer, "%d", resItem)

	// 		if i != len(res)-1 {
	// 			fmt.Fprintf(writer, " ")
	// 		}
	// 	}

	// 	fmt.Fprintf(writer, "\n")

	// 	writer.Flush()
}

// func readLine(reader *bufio.Reader) string {
// 	str, _, err := reader.ReadLine()
// 	if err == io.EOF {
// 		return ""
// 	}

// 	return strings.TrimRight(string(str), "\r\n")
// }

// func checkError(err error) {
// 	if err != nil {
// 		panic(err)
// 	}
// }
