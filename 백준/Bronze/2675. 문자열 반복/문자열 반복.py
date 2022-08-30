T = int(input())

for t in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)

    for i in S:
        print(R*i, end="")
    print()