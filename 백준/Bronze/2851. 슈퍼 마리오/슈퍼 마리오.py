list = []
for i in range(10):
    list.append(int(input()))

score, cursor = 0, 0

while True:
    score += list[cursor]
    try:
        if abs(100 - (score + list[cursor+1])) > 100 - score:
            break
    except:
        break
    cursor += 1

print(score)
