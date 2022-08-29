testCase = int(input())

for i in range(testCase):
    c, v = map(int, input().split()) # c: 사탕의 개수 / v: 형제의 수
    if 1 <= c and v <= 1000:
        v_get = c // v
        d_get = c % v
        print("You get {} piece(s) and your dad gets {} piece(s)."
              .format(v_get, d_get))