S = int(input())

for i in range(1, S + 1):
        space = " " * (S - i)
        star = "*" * i
        print(space + star)