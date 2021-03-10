#пользователь выбирает валюту
currency = input("Выберите валюту: рубли, доллары или евро: ")
change = input("Выберите валюту, в которую надо перевести: рубли, доллары или евро: ")
money = int(input("Введите количество денег: "))
#конвертация валюты
if currency == "рубли" and change == "евро":
    print(money, "рублей = ", money*0.011,"евро")
elif currency == "рубли" and change == "доллары":
    print(money, "рублей = ", money * 0.014, "долларов")
elif currency == "евро" and change == "доллары":
    print(money, "евро = ", money * 1.19, "долларов")
elif currency == "евро" and change == "рубли":
    print(money, "евро = ", money * 87.7, "рублей")
elif currency == "доллары" and change == "рубли":
    print(money, "долларов = ", money * 73.74, "рублей")
elif currency == "доллары" and change == "евро":
    print(money, "долларов = ", money * 0.84, "евро")