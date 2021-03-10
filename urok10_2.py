#пользователь вводит любое число больше 9
chislo = input("Введите целое число больше 9: ")
for a in chislo:
    if int(a) != 3 and int(a) !=6 :
        print(a, end="")

