#пользователь вводит числа от 1 до 100
chislo = int(input("Введите число от 1 до 100 включительно: "))
#если кратно трём
if chislo%3 == 0 and chislo%5 ==0 and chislo >=1 and chislo <=100:print("Fizz Buzz")
elif chislo%3 == 0 and chislo >=1 and chislo <=100:print("Fizz")
elif chislo%5 == 0 and chislo >=1 and chislo <=100:print("Buzz")
elif chislo >= 1 and chislo <= 100:print(chislo)
else:print("Ошибка. Число должно быть в диапазоне от 1 до 100 включительно")

###################################################################
#пользователь вводит количество продаж за месяц для трёх менеджеров
month1 = float(input("Введите количество продаж за месяц для первого менеджера: "))
month2 = float(input("Введите количество продаж за месяц для второго менеджера: "))
month3 = float(input("Введите количество продаж за месяц для третьего менеджера: "))
#зарплата первого менеджера
if month1 <500:salary1 = month1*0.03+200
elif month1 >=500 and month1 <1000:salary1 = month1*0.05+200
elif month1 >=1000:salary1 = month1*0.08+200
#зарплата второго менеджера
if month2 <500:salary2 = month2*0.03+200
elif month2 >=500 and month2 <1000:salary2 = month2*0.05+200
elif month2 >=1000:salary2 = month2*0.08+200
#зарплата третьего менеджера
if month3 <500:salary3 = month3*0.03+200
elif month3 >=500 and month3 <1000:salary3 = month3*0.05+200
elif month3 >=1000:salary3 = month3*0.08+200
#определение лучшего
best = max(salary1,salary2,salary3)
#начислить премию
if best == salary1:
    salary1=salary1+200
    print("Первый менеджер стал лучшим")
if best == salary2:
    salary2=salary2+200
    print("Второй менеджер стал лучшим")
if best == salary3:
    salary3=salary3+200
    print("Третий менеджер стал лучшим")
#зарплата всех
print("Первый менеджер получает: ", salary1, "\nВторой менеджер получает: ", salary2, "\nТретий менеджер получает: ", salary3)


#########################################################
#второе задание, пользователь вводит номер месяца
mesyaz = str(input("Введите номер месяца (от 1 до 12): "))
#когда у нас зима
if mesyaz == "1" or mesyaz == "2" or mesyaz == "12" : print("Winter")
#когда у нас весна
elif mesyaz == "3" or mesyaz == "4" or mesyaz == "5":print("Spring")
#когда у нас лето
elif mesyaz == "6" or mesyaz == "7" or mesyaz == "8":print("Summer")
#когда у нас осень
else: print("Autumn")