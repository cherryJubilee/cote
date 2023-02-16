# 풀이 1
n, m = map(int, input().split())

result = 0

while True:
    target = (n//m)*m  # n=41 m=3 target = 39  3의배수로 만들어주는 과정  (3의 배수가 아닌 경우)
    result += (n - target)  # result = 2, 3의 배수만큼을 뺸 나머지 (1씩 뺴는거니까 횟수론 2번)
    n = target  # n = 39 (이제 3의 배수가 됨.)
    if n < m:
        break
    result += 1  # 2+1=3
    n //= m      # n = 39//3 =13

result += (n-1)
print(result)


while True:
    target = (n//m)*m  # n=42 m=3 target = 42  3의배수로 만들어주는 과정 (이미 3의 배수인 경우)
    result += (n - target)  # result=0
    n = target  # n = 42
    if n < m:
        break
    result += 1  # 0+1=1  -> 1+2= 3 -> 3+1 = 4
    n //= m      # n = 42//3 =14 -> 4 -> 1

result += (n-1)  # -> 4≠
print(result)
