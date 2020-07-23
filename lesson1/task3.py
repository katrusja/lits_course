import random
print('Давай зіграємо гру "Вгадай число"')

a = int(input('Введи нижню межу діапазону чисел '))
b = int(input("Введіть верхню межу діапазону чисел "))
print('Діапазон', a, '...', b)

number = random.randint(a,b)

while True:
  s = int(input('Вгадай загадане число '))
  if s ==number:
    print('Ура! Ти вгадав!')
    break
  elif s >= number:
    print('Загадане число менше')
  elif s <= number:
    print('Загадане число більше')
