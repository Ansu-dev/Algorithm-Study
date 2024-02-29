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

	var N int
	fmt.Fscan(reader, &N)


	// TODO : 666부터 반복문을 돌면서 N번째에 해당하는 종말의 수가 포함되면 break
	// * 666이라는 문자열이 포함이 되는지 확인

	i := 666
	count := 0
	var result int
    for {
        if strings.Contains(strconv.Itoa(i), "666") {
			count++
			if count == N {
				result = i
				break
			}
		}
        i++
    }

	fmt.Fprintln(writer, result)
}