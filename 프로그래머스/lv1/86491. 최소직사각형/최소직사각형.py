def solution(sizes):
    big = []
    small =[] 
    for size in sizes:
        if size[0] > size[1]:
            big.append(size[0])
            small.append(size[1])
        else:
             big.append(size[1]) 
             small.append(size[0])
                         
    return max(big) * max(small)



"""
가로, 세로에서 둘 중 큰 값을 big =[]
작은 값을 small=[]에 넣고,
big중에 제일 큰 값과 small 중에 제일 큰 값을 곱하면 될 듯

아니면 들어오는 모든 리스트를 반으로 나눠서 큰것중에 큰 것 * 작은것 중에 큰 것 
가로, 세로를 신경쓰지 않는것이 중요함
"""