melody = list(map(int, input().split()))

def song(melody):
    i = 0
    while i < len(melody) - 1:
        if melody[i] - melody[i + 1] == -1 or melody[i] - melody[i + 1] == 1:
            i += 1
        else:
            return print("mixed")
    if melody[0] == 1:
        return print("ascending")
    if melody[0] == 8:
        return print("descending")

song(melody)