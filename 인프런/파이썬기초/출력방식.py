# 출력 방식
a,b,c = 1,2,3
print(a,b,c)   # 1 2 3
# sep에 설정한 형식 대로 띄워서 출력됨
print(a,b,c, sep=",")  # 1,2,3
print(a,b,c, sep=", ")  # 1, 2, 3
print(a,b,c, sep="")  # 123
print(a,b,c, sep=" ")  # 1 2 3
print(a,b,c, sep="\n")  
'''
1
2
3
'''

# print는 자동으로 줄바꿈 되는데, 한 행에 출력 하고싶을 때
# 1,2,3
print(a, end=",") 
print(b, end=",") 
print(c) 

# 변수입력과 연산자
a,b = input("숫자를 입력하세요: ").split()
c = a+b
print(type(c)) # <class 'str'>
print(c)       # 23

# int형으로 바꿔주어야 연산 가능
a = int(a)
b = int(b)
c = a+b
print(type(c)) # <class 'int'>
print(c)       # 5

# int형 쓰기 귀찮을 때  map사용하자
a, b = map(int, input("숫자를 입력하세요: ").split())
print(a+b)  # 5
print(a-b)
print(a*b)
print(a/b)
print(a//b) # 몫
print(a%b) # 나머지
print(a**b) # 제곱


# 반목문 (for, while)
a = range(10) 
print(list(a))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 11, 2):
    print(i)
'''
1
3
5
7
9
'''
i = 1
while i < 11:
    print(i)
    i += 2
'''
1
3
5
7
9
'''

# break : 해당 되면 멈춤
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
'''
1
2
3
4
5
'''

# continue: 해당하면 아래 코드 실행x
i = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue # 짝수이면 출력 하지 마
    print(i)
    