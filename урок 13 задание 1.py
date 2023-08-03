def pl(t):
    for i in t:
        print(*i)
shirina = int(input())
vysota = int(input())
import random  

X = [[random.randint(-10, 100) for i in range(shirina)] for i in range(vysota)]
print(" Матрица 1")
pl(X) 
Y = [[random.randint(-8, 90) for i in range(shirina)] for i in range(vysota)]
print(" Матрица 2")
pl(Y)
m = [[0 for i in range(shirina)] for i in range(vysota)]
print(" Матрица 3") 
for i in range(len(X)): 

   for j in range(len(X[0])): 
              m[i][j] = X[i][j] + Y[i][j] 

for r in m: 
      print(r) 


