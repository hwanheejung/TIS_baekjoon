while True:
    n = input()
    num = list(n)

    if n == "0":
        break
    elif num == num[::-1]:
        print("yes")
    else:
        print("no")