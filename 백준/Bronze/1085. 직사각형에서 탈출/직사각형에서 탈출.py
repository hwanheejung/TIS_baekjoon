x, y, w, h = map(int, input().split())
shortCut = []

if 1 <= x <= w - 1 and 1 <= y <= h - 1:
    shortCut.append(x)
    shortCut.append(y)
    shortCut.append(w - x)
    shortCut.append(h - y)
    print(min(shortCut))
else:
    pass