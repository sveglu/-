
    
 
n=int(input("Введите количество элементов списка "))

sp = list(map(int, input().split()))[:n]

e=set(sp)

print(len(e))
