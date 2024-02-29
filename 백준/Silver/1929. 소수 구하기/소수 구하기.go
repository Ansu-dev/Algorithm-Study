package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)


func isPrime(n int) bool {
	// 2는 소수이므로 예외 처리
	if n == 2 {
		return true
	}
	// 주어진 숫자가 2보다 작거나 음수이면 소수가 아님
	if n <= 1 || n % 2 == 0 {
		return false
	}
	// 3부터 주어진 숫자의 제곱근까지의 모든 홀수로 나누어보며 소수 여부를 확인
	// ! 소수가 아닌 수를 걸러내는 최적의 수
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		if n % i == 0 {
			return false // 나누어 떨어지는 수가 있으면 소수가 아님
		}
	}
	return true // 나누어 떨어지는 수가 없으면 소수임
}



func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N, M int
	fmt.Fscanf(reader, "%d %d", &N, &M)

	for i := N; i <= M; i++ {
		if isPrime(i) {
			fmt.Fprintln(writer, i)
		}
	}
}