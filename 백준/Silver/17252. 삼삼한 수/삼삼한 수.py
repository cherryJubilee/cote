num = int(input())

verify = True

if num == 0:        
    verify = False

while num > 0:
    if num % 3 == 2:      
        verify = False
    num //= 3    


if verify is True: 
    print("YES")   
else:
    print("NO")