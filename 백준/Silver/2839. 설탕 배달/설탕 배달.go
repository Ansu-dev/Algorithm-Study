package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N int
	fmt.Fscan(reader, &N)

	var result int;

	// 5로 나누어 떨어지는지 확인 아니라면 5로 나누고 나머지가 3으로 나누어떨어지는지 확인
	// 만약 5로 나누어 떨어지지 않는다면 5kg의 몫의 수에서 1개씩 줄여가며 3으로 나누어떨어지는지 확인
	// 5나 3으로 모두 나누어 떨어지지 않는다면 -1

	sugar5kg := 5
	sugar3kg := 3

	bag5kg := N / sugar5kg
	remainder := N % sugar5kg

	for bag5kg >= 0 {
		if remainder % sugar3kg == 0 {
			bag3kg := remainder / sugar3kg
			result = bag5kg + bag3kg
			fmt.Fprintln(writer, result)
			return
		}
		bag5kg--
		remainder += sugar5kg
	}

	result = -1
	fmt.Fprintln(writer, result)
}