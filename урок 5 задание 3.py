inv=int(input())
A=int(input())
B=int(input())
if ((A>=inv)and (B>=inv)):
    print(2)
elif (A>=inv):
    print("Mike")
elif B>=inv:
    print("Ivan")
elif B+A>=inv:
    print(1)
else:
    print("0")
