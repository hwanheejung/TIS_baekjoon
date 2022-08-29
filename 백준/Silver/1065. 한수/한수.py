N = int(input())
num = 0         # 한수의 개수
X = 1


def hansu(X):
    lstX = list(map(int, str(X)))
    # len(lstX) : index 개수 / 1->1~9 , 2->10~99 , 3->100~999 , ...

    if len(lstX) == 1:
        return 1
    if len(lstX) == 2:
        return 1

    elif len(lstX) >= 3:
        i = lstX[1] - lstX[0]
        for n in range(1, len(lstX), 1):
            if lstX[n] == lstX[0] + (n * i):
                pass
            else:
                return 0
        return 1

    else:
        return 0


while X <= N:
    if hansu(X) == 1:
        num += 1
    elif hansu(X) == 0:
        pass
    X += 1

print(num)