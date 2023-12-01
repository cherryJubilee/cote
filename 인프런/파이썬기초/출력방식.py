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