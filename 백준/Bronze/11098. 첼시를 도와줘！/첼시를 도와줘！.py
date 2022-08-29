n = int(input())

for f in range(n):
    p = int(input())
    playerCost = []
    playerName = []
    for i in range(p):
        C, name = input().split()
        playerCost.append(int(C))
        playerName.append(name)

    maxIdx = playerCost.index(max(playerCost))
    print(playerName[maxIdx])