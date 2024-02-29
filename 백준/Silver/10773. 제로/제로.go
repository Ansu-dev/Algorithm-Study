package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)


type Stack []int

func (s *Stack) Push(item int) {
	(*s) = append((*s), item)
}

// 스택에서 요소를 제거하고 반환하는 pop 연산 구현
func (s *Stack) Pop() {
	(*s) = (*s)[:len(*s)-1]
}


func (arr *Stack) Sum() int {
	sum := 0
	for _, num := range *arr {
		sum += num
	}
	return sum
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var K int
	fmt.Fscanf(reader, "%d\n", &K)

	var numbers Stack
	for i :=0; i < K; i++ {
		numberStr, _ := reader.ReadString('\n')
		numberStr = strings.TrimSuffix(numberStr, "\n")
		number, _ := strconv.Atoi(numberStr)
		if number == 0 {
			// * number가 0일 경우 무조건 지울수 있는 수가 존재한다를 가정
			numbers.Pop()
			continue
		}
		numbers.Push(number)
	}

	fmt.Fprintln(writer, numbers.Sum())
}