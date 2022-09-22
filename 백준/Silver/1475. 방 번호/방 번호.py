N = list(map(int, input()))
cnt = [0] * 9

for n in N:
    if n == 9:
        n = 6
    cnt[n] += 1

if cnt[6] % 2 == 0:
    cnt[6] = cnt[6] // 2
else:
    cnt[6] = cnt[6] // 2 + 1

print(max(cnt))