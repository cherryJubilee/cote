# [1149] RGB거리

# 입력 받기
num = int(input())
# costs = [list(map(int, input().split())) for _ in range(num)]
costs = []
for i in range(num):
    rgb_costs = list(map(int, input().split()))
    costs.append(rgb_costs)


def dp(num, costs):
    # N x 3 크기의 2차원 배열 만들기
    dp = [[0] * 3 for _ in range(num)]

    for i in range(num):
        for j in range(3):
            if i == 0:
                dp[i][j] = costs[i][j]
            else:
                dp[i][j] = costs[i][j] + \
                    min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3])

    return min(dp[num-1])


# 출력
print(dp(num, costs))
