#задание1
#Пользователь вводит количество недель, месяцев, лет и получает количество дней за это время.
week = int(input("Введите количество недель: "))
month = int(input("Введите количество месяцев: "))
year = int(input("Введите количество лет: "))
#считаем дни
day1 = week*7
day2 = month*30
day3 = year*365
#выводим результат
print("Это будет: ",day1+day2+day3, "дней")

#задание2
#Пользователь вводит три числа
chislo1 = int(input("Введите первое число: "))
chislo2 = int(input("Введите второе число: "))
chislo3 = int(input("Введите третье число: "))
#Увеличьте первое число в два раза, второе число уменьшите на 3, третье число возведите в квадрат
resultat1 = chislo1*2
resultat2 = chislo2-3
resultat3 = chislo3**2
#и затем найдите сумму новых трех чисел
print("Сумма трех чисел: ",resultat1+resultat2+resultat3)

#задание3
#Пользователь вводит два числа.
chislo1 = int(input("Введите первое число: "))
chislo2 = int(input("Введите второе число: "))
#Если каждое из них не равно 10 и первое число четное, то вывести их сумму, иначе вывести их произведение.
if chislo1%2 == 0:
    if chislo1 !=10 and chislo2 !=10:
        print("Сумма чисел: ", chislo1+chislo2)
    else: print("Произведение чисел: ",chislo1*chislo2)
else: print("Произведение чисел: ",chislo1*chislo2)


#задание4
#Сформировать строку из 10 символов - 5 четных цифр и 5 букв.
stroka1 = list(input("Введите 5 чётных цифр:"))
stroka2 = list(input("Введите 5 букв: "))
otvet =[]
#На четных позициях должны находится четные цифры, на нечетных позициях - буквы.
for a in range(0,5):
    otvet.append(stroka2[a])
    otvet.append(stroka1[a])
print("Строка:","".join(otvet))

#задание5
#Пользователь вводит строку
stroka = input("Введите строку: ")
count1=0
count2=0
#Определите, какой символ в ней встречается раньше: 'x' или 'w'
#Если какого-то из символов нет, вывести сообщение об этом.
if "x" not in stroka or "w" not in stroka:
    print("Нет нужного символа")
else:
    for a in stroka:
        if a == "x":
            count1=stroka.index(a)
        if a == "w":
            count2=stroka.index(a)
    if count1<count2:
        print("Символ x встречается раньше")
    else:
        print("Символ w встречается раньше")

#задание6
#Вывести ряд чисел: десять десяток, девять девяток, восемь восьмерок, ... , одну единицу.
spisok = []
for a in range(10,0,-1):
    stroka = ""
    for b in range(a,0,-1):
        stroka=stroka+str(a)
    print(stroka)
    spisok.append(int(stroka))
#Найти сумму всех этих чисел
print("Сумма этих чисел: ",sum(spisok))









