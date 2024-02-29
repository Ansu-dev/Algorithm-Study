package main

import (
	"bufio"
	"fmt"
	"os"
)

type Graph1260 struct {
	graph     [][]bool
	isVisited []bool
	result    []int
}

func (g *Graph1260) reset1260(n int) {
	g.isVisited = make([]bool, n+1)
	g.result = []int{}
}

func (g *Graph1260) print1260() {
	for i, v := range g.result {
		fmt.Print(v)
		if i < len(g.result)-1 {
			fmt.Print(" ")
		}
	}
}

func main() {
	var n, m, v int
	var read = bufio.NewReader(os.Stdin)
	fmt.Fscanln(read, &n, &m, &v)

	var graph1260 = Graph1260{
		graph:     make([][]bool, n+1),
		isVisited: make([]bool, n+1),
	}

	for i := range graph1260.graph {
		graph1260.graph[i] = make([]bool, n+1)
	}

	for i := 0; i < m; i++ {
		var p1, p2 int
		fmt.Fscanln(read, &p1, &p2)

		graph1260.graph[p1][p2] = true
		graph1260.graph[p2][p1] = true
	}

	dfs1260(v, &graph1260)
	graph1260.print1260()
	fmt.Println()

	graph1260.reset1260(n)

	bfs1260(v, &graph1260)
	graph1260.print1260()
}

func dfs1260(v int, graph1260 *Graph1260) {
	graph1260.isVisited[v] = true
	graph1260.result = append(graph1260.result, v)

	for i := 0; i < len(graph1260.graph[v]); i++ {
		if graph1260.graph[v][i] && !graph1260.isVisited[i] {
			dfs1260(i, graph1260)
		}
	}
}

func bfs1260(v int, graph1260 *Graph1260) {
	graph1260.isVisited[v] = true
	q := []int{v}

	for {
		if len(q) == 0 {
			return
		}

		f := q[0]
		q = q[1:]
		graph1260.result = append(graph1260.result, f)

		for i := 0; i < len(graph1260.graph[v]); i++ {
			if graph1260.graph[f][i] && !graph1260.isVisited[i] {
				graph1260.isVisited[i] = true
				q = append(q, i)
			}
		}
	}
}