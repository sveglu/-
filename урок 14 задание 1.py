def tmp(x):
    if x<0:
        return
    tmp(x-1)
   
    print(x)
    
n=int(input())
tmp(n)

print("Конец списка")    
       

