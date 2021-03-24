#Игра крестики-нолики. Поля 3х3, реализуется через двухмерный массив (вложенные списки)
#* - пустое поле
#Х - крестик
#0 - нолик
pole = []#поле
for a in range (3):
    row = [EMPTY for a in range(3)]
    pole.append(row)
koordinati = []#координаты, которые будут меняться
komanda =  input("Перед вами поле 3х3. Введите команду: крест, ноль или стоп: ")
if komanda = "крест" or komanda = "ноль":
    b = input("Введите координаты: ")
    koordinati.append(b)
    if len(koordinati)>3 or len(koordinati)<1:
        print("Таких координат не существует")

elif komanda = "стоп":
    break










