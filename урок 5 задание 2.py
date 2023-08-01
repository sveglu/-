print("Введите любое латинское слово")
s=input()
gl=0
sogl=0
for i in range(len(s)):
    if s[i] in "aeiou":
        gl+=1
    else:
        sogl+=1
print("Количество гласных букв =", gl)
print("Количество согласных букв =", sogl)
print("Количество букв а =", s.count('a'),"Количество букв e =", s.count('e'),"Количество букв i =", s.count('i'), "Количество букв o =", s.count('o'),"Количество букв u =", s.count('u'))
