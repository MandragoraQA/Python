#пользователь вводит 6значное число
chislo = input("Введите шестизначное чсло: ")
def lucky(chislo):
    summa1 = sum([chislo[:3]])
    summa2 = sum([chislo[3:]])
    if summa1 == summa2:
        return True
    else:
        return False
lucky(chislo)









