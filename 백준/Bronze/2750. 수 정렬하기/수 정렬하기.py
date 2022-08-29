N = int(input())
num = []
for i in range(N):
    n = int(input())
    num.append(n)
    
"""bubble sort"""
idx = 0
while idx <= len(num) - 2:
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            blank = num[i]
            num[i] = num[i+1]
            num[i+1] = blank
    idx += 1

for i in range(len(num)):
    print(num[i])