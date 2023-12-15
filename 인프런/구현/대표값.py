n = int(input())
num_list = list(map(int, input().split()))

num_sum = round(sum(num_list) / n, 1)
print(num_sum)

