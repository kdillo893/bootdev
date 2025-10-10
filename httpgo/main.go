package main

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"os"
)

func getLinesChannel(f io.ReadCloser) <-chan string {
	out := make(chan string, 1)

	//close when channel is done sending
	go func() {
		defer f.Close()
		defer close(out)

		//put byte string segments into out, emit them on the channel
		var line string
		for {
			data := make([]byte, 8)
			n, err := f.Read(data)
			if err != nil {
				break
			}

			data = data[:n]
			for i := bytes.IndexByte(data, '\n'); i >= 0; {
				line += string(data[:i])
				data = data[i+1:]
				out <- string(line)
				line = ""

				//also check in case of multiple \n
				i = bytes.IndexByte(data, '\n')
			}

			line += string(data)
		}

		if len(line) != 0 {
			out <- string(line)
		}

	}()

	return out
}

func main() {

	file, err := os.Open("messages.txt")
	if err != nil {
		log.Fatal("error", "could not open file", err)
	}

	lines := getLinesChannel(file)
	for line := range lines {
		fmt.Printf("read: %s\n", line)

	}

	// var line string
	// for {
	// 	data := make([]byte, 8)
	// 	n, err := file.Read(data)
	// 	if err != nil {
	// 		break
	// 	}
	//
	// 	data = data[:n]
	// 	for i := bytes.IndexByte(data, '\n'); i >= 0; {
	// 		line += string(data[:i])
	// 		data = data[i+1:]
	// 		fmt.Printf("read: %s\n", line)
	// 		line = ""
	//
	// 		//also check in case of multiple \n
	// 		i = bytes.IndexByte(data, '\n')
	// 	}
	//
	// 	line += string(data)
	// }
	//
	// if len(line) != 0 {
	// 	fmt.Printf("read: %s\n", line)
	// }
}
