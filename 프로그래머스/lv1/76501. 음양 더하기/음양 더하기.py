def solution(absolutes, signs):
    print(signs)

    sum = 0
    for i in range(len(absolutes)):
        
        if signs[i] == True:   # "true"
            sum += absolutes[i]
        elif signs[i] == False:   # "false"
            sum -= absolutes[i] 
            
  
    return sum