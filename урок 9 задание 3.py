
n = [int(s) for s in input().split()]
used = set()
for num in n:
    if num in used:
        print('YES')
    else:
        print('NO')
        used.add(num)    
 




 
