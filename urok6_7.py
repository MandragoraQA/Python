#пользователь вводит цену и количество товара
zena = float(input("Введите цену одного товара: "))
skolko = int(input("Введите количество товара: "))
#определить скидку
if skolko > 5 and skolko <= 10: print("Итоговая стоимость со скидкой: " + str(round(zena/100*75*skolko, 0))) #25%
elif skolko > 10: print("Итоговая стоимость со скидкой: " + str(round(zena/100*50*skolko, 0))) #50%
else:print("Итоговая стоимость со скидкой: " + str(round(zena*skolko, 0)))#без скидки