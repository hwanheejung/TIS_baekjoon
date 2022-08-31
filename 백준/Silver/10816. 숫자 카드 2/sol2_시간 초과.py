import sys
M = sys.stdin.readline()
M_li = list(map(int, sys.stdin.readline().split()))

# 상근이가 가지고 있는 카드
N = int, sys.stdin.readline()
N_li = list(map(int, sys.stdin.readline().split()))

num = []
for n in N_li:
    cardNum = 0
    for i in range(len(M_li)):
        if M_li[i] == n:
            cardNum += 1
    num.append(cardNum)
print(*num)
