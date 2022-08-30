T = int(input())

for t in range(T):
    score = []
    li = list(input())
    num = 0
    for idx in range(len(li)):
        if li[idx] == "O":
            num += 1
            score.append(num)
        elif li[idx] == "X":
            num = 0
    print(sum(score))