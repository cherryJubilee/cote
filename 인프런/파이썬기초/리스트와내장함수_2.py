a = [23, 12, 36, 53, 19]

# 튜플
for i in enumerate(a):
    print(i)
'''
(0, 23)
(1, 12)
(2, 36)
(3, 53)
(4, 19)
'''

# [리스트]는 값을 변경 가능하지만 (튜플)은 값을 변경 불가능
b = (1,2,3,4,5)
# b[0] = 7   # 안됨
# print(b) 'tuple' object does not support item assignment

for x in enumerate(a):
    print(x[0], x[1])
print()
'''
print(x)
(0, 23)
(1, 12)
(2, 36)
(3, 53)
(4, 19)
print(x[0], x[1])
0 23
1 12
2 36
3 53
4 19
'''

# 보통 사용하는 방법 
for index, val in enumerate(a):
    print(index, val)
print()
'''
0 23
1 12
2 36
3 53
4 19
'''

# all : 모든 것이 참
if all(x<50 for x in a):
    print("yes")
else:
    print("no")  # no
# any : 한개라도 참
if any(x<20 for x in a):
    print("yes")
else:
    print("no")  # yes