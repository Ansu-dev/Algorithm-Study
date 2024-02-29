package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)


func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	// * K : 타깃, N : 목표 -> 이분탐색
	var K, N int
	fmt.Fscanf(reader, "%d %d\n", &K, &N)

	
	var numbers []int
	for i := 0; i < K; i++  {
		numberStr, _ := reader.ReadString('\n')
		numberStr = strings.TrimSuffix(numberStr, "\n")
		number, _ := strconv.Atoi(numberStr)
		numbers = append(numbers, number)
	}

	// TODO : 최소, 최대 길이를 판별
	// TODO : 주어진 길이로 만들수 있는 랜선의 개수 반환

	left, right := 1, maxLength(numbers)
	result := 0
	// * 이분탐색 수행
	for left <= right {
		mid := (left + right) / 2
		if N <= countLines(numbers, mid) { // 만들 수 있는 랜선의 개수가 목표보다 크거나 같은 경우
			result = mid // * 현재의 길이를 저장
			left = mid + 1 // * 최소 길이를 mid + 1로 갱신하여 더 큰 길이를 찾음
			continue
		}
		right = mid - 1 // * 만들 수 있는 랜선의 개수가 목표보다 작은 경우, 최대 길이를 줄여서 더 작은 길이를 찾음
	}

	fmt.Fprintln(writer, result)

}

func maxLength(numbers []int) int {
	max := numbers[0]
	for _, number := range numbers {
		if max < number {
			max = number
		}
	}
	return max
}

func countLines(numbers []int, length int) int {
	count := 0
	for _, number := range numbers {
		count += number / length // * 랜선에서 주어진 길이를 나누어 개수를 누적함
	}
	return count
}