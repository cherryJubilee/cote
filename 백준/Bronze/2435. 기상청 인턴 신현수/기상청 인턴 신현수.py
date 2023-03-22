N, K = map(int, input().split()) 
temps = list(map(int, input().split())) 

temps_sum = []
for i in range(N-K+1): 
    sum = 0
    for j in range(i, i+K):  
        sum += temps[j]
    temps_sum.append(sum)


print(max(temps_sum))