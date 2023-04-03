viruchka = int(input("Введите выручку фирмы:"))
izderzki = int(input("Введите издержки фирмы:"))
pribil =  viruchka - izderzki
rentab = pribil/viruchka
print("Прибыль:{0}, рентабельность:{0}".format(pribil, rentab))
if viruchka>izderzki:
    print("Вы в плюсе. Пока что...")
elif viruchka<izderzki:
    print("Вы в минусе. Возможно в следующем месяце повезёт больше")

else:
    print("вы на нуле.")

sotrudnik = int(input("Введите кол-во сотрудников:"))
pribil_sotrudnik = pribil/sotrudnik

print("Прибыль на сотрудника:{0}".format(pribil_sotrudnik))