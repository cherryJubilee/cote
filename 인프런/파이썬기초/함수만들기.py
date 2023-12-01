''' 
함수 
- 항상 함수를 먼저 선언하고 main script 에서 사용하기
- 함수는 여러개의 값을 리턴할 수 있다
'''

# return : 함수 안에서 값을 리턴하고 종료하는 역할
def add(a,b):
    c = a+b
    return c

x = add(3,2)
print(x)  # 5


def add(a,b):
    c = a+b
    d = a-b
    return c, d
print(add(5,2))  # (7, 3) 튜플 자료구조로 출력


# 소수 출력하는 함수
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False # 나눠지는게 있는 경우 소수가 아니니까 return 해서 함수 종료
    return True # 나눠지는게 없는 경우 소수이다


a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y): # 참(True)이라면 
        print(y, end=" ")

