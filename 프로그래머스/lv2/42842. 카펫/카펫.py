def solution(brown, yellow):
    
    yellow_x = 0
    yellow_y = 0
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
    
        if (yellow_x + 2) *  (yellow_y + 2) - (yellow_x * yellow_y) == brown:
            return [yellow_x+2, yellow_y+2]            
        

            
