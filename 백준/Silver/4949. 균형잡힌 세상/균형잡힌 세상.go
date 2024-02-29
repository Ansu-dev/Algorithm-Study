package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Stack []string

func (s *Stack) Push(item string) {
	(*s) = append((*s), item)
}

func (s *Stack) Pop() {
	(*s) = (*s)[:len(*s)-1]
}

func (s *Stack) Size() int {
    return len(*s)
}

func (s *Stack) Last() string {
    data := (*s)[len(*s)-1]
	return data
}


func validators(s string) bool{
	splits := strings.Split(s, "")
	brackets := make(Stack, 0)
	for _, split := range splits {
		if split == "(" {
			brackets.Push(split)
		} else if split == ")" {
			if brackets.Size() == 0 || brackets.Last() != "("{
				return false
			}
			brackets.Pop()
		} else if split == "[" {
			brackets.Push(split)
		} else if split == "]" {
			if brackets.Size() == 0 || brackets.Last() != "[" {
				return false
			}
			brackets.Pop()
		}
	}
	if brackets.Size() == 0{
		return true
	}

	return false
}


func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var results []string

	for {
		word, _ := reader.ReadString('\n')
		word = strings.TrimSuffix(word, "\n")
		if word == "." {
			break
		}

		if validators(word) {
			results = append(results, "yes")
		} else {
			results = append(results, "no")
		}
	}


	for _, result := range results {
		fmt.Fprintln(writer, result)
	}

}