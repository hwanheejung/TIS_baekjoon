N = int(input())
score = list(map(int, input().split()))
score.sort()
fake = []

M = score[-1]

for i in range(len(score)):
    fakeScore = score[i] / M * 100
    fake.append(fakeScore)

res = sum(fake) / N
print(res)