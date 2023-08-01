
    
 
n1=int(input("Введите количество элементов первого списка "))

sp1 = list(map(int, input().split()))[:n1]

e1=set(sp1)



n2=int(input("Введите количество элементов второго списка "))

sp2 = list(map(int, input().split()))[:n2]

e2=set(sp2)

print(len(e1.union(e2)))
