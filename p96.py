# 풀이 1
row, col = map(int, input().split())

result = 0
for _ in range(row):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)

# 풀이 2
# 각 숫자는 1이상 10000이하의 자연수 임.
row, col = map(int, input().split())

result = 0
for _ in range(row):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)
