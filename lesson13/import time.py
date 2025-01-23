import time
print("тест: из какой ты групировки сталкер?")
print("введите свое имя")
name = input()
print(name,"нажмите Enter, чтобы начать раследование!")
start = input()

Svoboda = 0
Dolg = 0
Monolit = 0
Odinochki = 0
Zombie = 0

print("1) Какой цвет вам нравится больше?")
print("1 - зеленый, 2 - красный, 3 - голубой, 4 - желтый")
answer = int(input())

if answer == 1:
    Svoboda += 1
    Monolit += 1
elif answer == 2:
    Dolg += 1
    Odinochki += 1
elif answer == 3:
    Monolit += 1
else:
    Odinochki += 1

print("2) Вы часто убивайте зараженых?")
print("1 - да, 2 - нет")
answer = int(input())
if answer == 1:
    Svoboda += 1
    Monolit += 1
    Dolg += 1
    Odinochki += 1
else:
    Zombie += 1

print("3) Вы часто ходите к Сидоровичу?")
print("1 - да, 2 - нет")
answer = int(input())
if answer == 1:
    Odinochki += 1
else:
    Svoboda += 1
    Monolit += 1
    Dolg += 1
    Zombie += 1
print("4) вы дружите с Монолитом?")
print("1 - да, 2 - нет")
answer = int(input())
if answer == 1:
    Monolit += 1
else:
    Svoboda += 1
    Dolg += 1
    Zombie += 1
    Odinochki += 1

print("5) вы дружите с одиночками(сталкерами)?")
print("1 - да, 2 - нет")
answer = int(input())
if answer == 1:
    Odinochki += 1
    Svoboda += 1
    Dolg += 1
else:
    Zombie += 1
    Monolit += 1
print("результаты будут сделаны через секунду")
time.sleep(1)

max = 0
if Monolit > max:
    max = Monolit
if Svoboda > max:
    max = Svoboda
if Dolg > max:
    max = Dolg
if Zombie > max:
    max = Zombie
if Odinochki > max:
    max = Odinochki

if Monolit == max:
    print("вы Монолит!")
if Svoboda == max:
    print("вы Свобода!")
if Dolg == max:
    print("вы Долг!")
if Zombie == max:
    print("вы зараженный!")
if Odinochki == max:
    print("вы Одиночка!")
