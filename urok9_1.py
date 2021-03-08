#пользователь вводит число
chislo = int(input("Введите число от 2 до 10: "))
if chislo >=2 or chislo >=10:
    for a in range (2, 10 +1):
        print(chislo, "*", a, "=", chislo*a)
else:int(input("Введите число от 2 до 10: "))