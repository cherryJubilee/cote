# list 만드는 방법
a = list()
b = [1,2,3,4,5]
print(a)
print(b)

c = list(range(6,11))
# print(c)
# [6, 7, 8, 9, 10]

sum_list = b + c
# print(sum_list) 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# append : list에 값 추가하기
b.append(6) # [1, 2, 3, 4, 5, 6]

# insert : 특정 지점에 값 추가
b.insert(3, 100) # [1, 2, 3, 100, 4, 5, 6]


# pop() : 맨 뒤부터 제거
b.pop()
print(b)

# pop(index) : 원하는 index 위치 제거
b.pop(0)
print(b)

# remove(4) : 4 제거
b.remove(4)

# sort : 정렬
b.sort() # 오름차순
b.sort(reverse=True) # 내림차순

