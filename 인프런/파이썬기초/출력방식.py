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


