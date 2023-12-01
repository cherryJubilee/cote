# 문자열
msg = "I am Hyewon Park"
print(msg.upper)
print(msg.lower)
print(msg)

# find -> 문자의 위치의 index 번호를 알려 줌
tmp = msg.upper()
print(tmp.find('A')) 
# count -> 문자 개수 알려 줌
print(tmp.count('A')) 

# 문자 slice 하기
print(msg[:4])   # I am
print(msg[3:5])   # m

# 문자열 접근 방법
print(len(msg)) 
for i in range(len(msg)):
    print(msg[i], end=" ")  # I   a m   H y e w o n   P a r k
print()

# 아스키 넘버 -> A:65 / Z:90
tmp = 'AZ'
for x in tmp:
    print(ord(x))
'''
65
90
'''
# 아스키 넘버 -> a:97 / z:122
tmp = 'az'
for x in tmp:
    print(ord(x))
'''
97
122
'''

# 아스키 넘버에 해당하는 문자 출력
tmp = 100
print(chr(tmp))  # d
