from itertools import product

def solution(word):
    b = []
    a = [ 'A', 'E', 'I', 'O', 'U']
    for i in range(1, len(a)+1):
        for words in product(a, repeat = i):
            # print(''.join(sort_word))
            b.append(''.join(words))
    b.sort()
    for i in range(len(b)):
        if word == b[i]:
            return i+1