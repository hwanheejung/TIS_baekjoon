H, M = map(int, input().split())

H = H % 24
M = M % 60

if M >= 45:
    print(H, M - 45)
elif M < 45:
    if H == 0:
        print(23, 60 + (M - 45))
    else:
        print(H - 1, 60 + (M - 45))