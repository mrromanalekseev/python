



print('Hello Mary Очень рад быть вашим студентом! Задание 6')

a = int(input('Сколько километров бегун пробежал в первый день? '))
b = int(input('Сколько километров бегун пробежал на x ден? '))
x = int((b - a) // (a / 10))
print(f'на {x} день бегун пробежал {b} километров')

#задание 5
print('Hello Mary Очень рад быть вашим студентом! Задание 5')
money = int(input('Выручка '))
honey = int(input('Издержки '))
while money > honey:
    print('Прибыль! ')
    box = (money - honey) / money
    print(f'рентабильность {box:.2f}')
    staff = int(input('Число сотрудников фирмы '))
    boxfor1 = (money - honey) // staff
    print(f'Прибыль на одного {boxfor1}')
    break
else:
    print('Убыток! ')


#задание 4
print('Hello Mary Очень рад быть вашим студентом! Задание 4')
n1 = int(input('Введите первую цифру двухзначного числа '))
n2 = int(input('Введите вторую цифру двухзначного числа '))
while n1 > n2:
    print(f'{n1} самая большая цифра в числе')
    break
else:
    print(f'{n2} самая большая цифра в числе')

#задание 3
print('Hello Mary Очень рад быть вашим студентом! Задание 3')
n = input('Enter number ')
b = n + n
c = n + n + n
sum = (int(n) + int(b) + int(c))
print(f'{sum}')

#задание 2
print('Hello Mary Очень рад быть вашим студентом! Задание 2')
sec = int(input('Enter time in seconds '))
min = sec // 60
hours = min // 60
print(f'{sec} секунд это {hours} hour или {min} min')

#задание 1
print('Hello Mary Очень рад быть вашим студентом! Задание 1')
first = int(input('Enter number a '))
second = int(input('Enter number b '))
third = int(input('Enter number c '))
print(f'{first} {second} {third} ')

