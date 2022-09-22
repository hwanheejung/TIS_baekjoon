import sys
N = int(sys.stdin.readline())
nameL = []
rev_nameL = []

for n in range(N):
    name = input()
    nameL.append(name)

for i in reversed(nameL):
    rev_nameL.append(i)

if nameL == sorted(nameL):
    print("INCREASING")
elif rev_nameL == sorted(nameL):
    print("DECREASING")
else:
    print("NEITHER")