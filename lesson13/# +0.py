
print('Приветсвтуем тебя на тесте: кто ты из винкс?')
print('Представься, пожалуйста!')
name = input()

print('Рады тебя видеть,',name,'! Давай приступим к тесту!')

stella = 0
blum = 0
leyla = 0
muza = 0

print('1) Какая погода тебе больше нравится?')
print('1 - солышко, 2 - дождь, 3 - снег')
otvet = int(input())
if otvet == 1:
    stella += 1
    blum +=1
elif otvet == 2:
    leyla += 1
else:
    muza += 1
    
print('2) Ты любишь слушать музыку?')
print('Напиши "да" или "нет"')
otvet = input()
if otvet == 'да':
    muza += 1
else:
    stella += 1
    blum +=1
    leyla += 1
    
max = 0
if stella > max:
    max = stella
if blum > max:
    max = blum
if leyla > max :
    max = leyla
if muza > max:
    max = muza
    
if max == stella:
    print('ты слелла')
if max == blum:
    print('ты блум')
if max == leyla:
    print('ты лейла')
if max == muza:
    print('ты муза')
 