package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)



type Stack []int

// 스택에 요소를 추가하는 push 연산 구현
func (s *Stack) Push(item int) {
	(*s) = append((*s), item)
}

// 스택에서 요소를 제거하고 반환하는 pop 연산 구현
func (s *Stack) Pop() int {
	if len(*s) != 0 {
		data := (*s)[len(*s)-1]
		(*s) = (*s)[:len(*s)-1]
		return data
	}
	return -1
}

func (s *Stack) Size() int {
    return len(*s)
}

func (s *Stack) IsEmpty() int {
	if len(*s) == 0 {
		return 1
	}
	return 0
}

func (s *Stack) Top() int {
	if s.IsEmpty() == 1 {
		return -1
	}
	return (*s)[s.Size()-1]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	// 명령의 수 N 입력받기
	var N int
	fmt.Fscanf(reader, "%d\n", &N)

	// 명령을 저장할 슬라이스 선언
	var commands []string

	// 명령 처리
	for i := 0; i < N; i++ {
		command, _ := reader.ReadString('\n')
		command = strings.TrimSuffix(command, "\n")
		// 명령을 슬라이스에 추가
		commands = append(commands, command)
	}


	stack := Stack{}
	for _, command := range commands {
		// TODO : command를 split 하여 문자열과 숫자를 분리
		// * [0] 인자의 command를 구분하여 command마다의 예외처리를 진행
		parts := strings.Split(command, " ")
		if parts[0] == "push" {
			item, _ := strconv.Atoi(parts[1])
			stack.Push(item)
		} else if parts[0] == "pop" {
			fmt.Fprintln(writer, stack.Pop())
		} else if parts[0] == "size" {
			fmt.Fprintln(writer, stack.Size())
		} else if parts[0] == "empty" {
			fmt.Fprintln(writer, stack.IsEmpty())
		} else {
			fmt.Fprintln(writer, stack.Top())
		}
	}
}