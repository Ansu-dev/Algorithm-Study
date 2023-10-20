# 많이 팔린책을 출력
# 많이 팔린책이 같은 책이 있다면 알파벳숫서가 작은걸 출력

d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:  # 이미 book이 이전에 등록이 되어있는지
        d[book] += 1
    else:
        d[book] = 1


# 배열을 통한 dictionary에서 많이 팔린책을 찾아내야함
m = max(d.values())
book = []
for k, v in d.items():
    if v == m:
        book.append(k)
# 가장많이 팔린책이 여러개이면 그중에서 알파벳의 순서가 낮은것
print(sorted(book)[0])
