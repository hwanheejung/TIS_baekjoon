T = int(input())

for _ in range(T):
    isVPS = 0       # 0: YES / else: NO
    PS = input()

    for ps in PS:
        if ps == "(":
            isVPS += 1
        elif ps == ")":
            if isVPS >= 1:
                isVPS -= 1
            else:   # ()만 성립. )(일 경우, NO
                print("NO")
                break
    else:
        if isVPS == 0:
            print("YES")
        else:
            print("NO")
            