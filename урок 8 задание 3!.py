m = int(input())
n = int(input())
a =[]
for _ in range(n):
    a.append(int(input()))
    
print((2 * min(a) <= m) + len([x for x in a if x + min(a) > m]))
