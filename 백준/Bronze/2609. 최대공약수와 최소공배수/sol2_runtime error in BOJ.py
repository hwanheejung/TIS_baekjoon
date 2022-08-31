import sys
A, B = map(int, sys.stdin.readline().split())

def divisor(X):
    li = []
    a = 1
    while a <= int(X**0.5):
        if X % a == 0:
            b = X // a
            li.append(a)
            li.append(b)
        a += 1
    return li

li_A = divisor(A)
li_B = divisor(B)

GCF = []
for i in li_A:
    if i == 1:
        pass
    elif i in li_B:
        GCF.append(i)

print(max(GCF))

x = A // max(GCF)
y = B // max(GCF)
LCM = max(GCF) * x * y
print(LCM)

