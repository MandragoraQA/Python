#пользователь вводит 4 числа
chislo_1 =int(input("Введите первое число: "))
chislo_2 =int(input("Введите второе число: "))
chislo_3 =int(input("Введите третье число: "))
chislo_4 =int(input("Введите четвёртое число: "))
#определить самое большое с max
bolshoe =print(max(chislo_1,chislo_2,chislo_3,chislo_4))
#определить самое большое через if
if chislo_1 > chislo_2 and chislo_1 > chislo_3 and chislo_1 > chislo_4:print(chislo_1)
elif chislo_2 > chislo_1 and chislo_2 > chislo_3 and chislo_2 > chislo_4:print(chislo_2)
elif chislo_3 > chislo_1 and chislo_3 > chislo_2 and chislo_3 > chislo_4:print(chislo_3)
else:print(chislo_4)