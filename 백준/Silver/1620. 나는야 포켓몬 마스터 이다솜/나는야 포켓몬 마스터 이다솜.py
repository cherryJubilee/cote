# [1620] 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_to_word = {}
word_to_num = {}

for i in range(1, N+1):
    word = input().strip()
    num_to_word[i] = word
    word_to_num[word] = i


for _ in range(M):
    word = input().strip()
    if word.isdigit():
        print(num_to_word[int(word)])
    else:
        print(word_to_num[word])
