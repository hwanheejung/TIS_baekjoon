while True:
    a, b, c = map(int, input().split())
    li = [a, b, c]
    li.sort()

    if a == 0 and b == 0 and c == 0:
        break
    else:
        if li[2]**2 == li[0]**2 + li[1]**2:
            print("right")
        else:
            print("wrong")