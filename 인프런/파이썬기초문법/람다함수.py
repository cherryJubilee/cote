# 함수
def plus_one(x):
    return x+1

print(plus_one(2))  # 3

# 람다함수, 람다표현식
plus_two = lambda x : x+2
print(plus_two(1)) # 3


# 자주 쓰는 람다 실 사용 방법
def plus_one(x):
    return x+1
a = [1,2,3]

# 함수사용 한 경우
print(list(map(plus_one, a)))  # [2, 3, 4]
# 람다 사용한 경우
print(list(map(lambda x:x+1, a)))  # [2, 3, 4]