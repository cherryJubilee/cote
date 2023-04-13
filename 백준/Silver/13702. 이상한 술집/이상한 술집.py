# [13702] 이상한 술집

# n 주전자의 개수
# k 인원수
n, m = map(int, input().split())
drink_list = [int(input()) for _ in range(n)]
start, end = 1, max(drink_list)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for drink in drink_list:
        total += (drink // mid)

    if total >= m:
        answer = mid
        start = mid+1
    else:
        end = mid-1


print(answer)
