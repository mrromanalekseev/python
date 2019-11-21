''' Number 7 '''

def fibo_gen(n):
    m = 1
    for a in range(1, n):
        if a > 15:
            break
        m *= a
        yield m


for i in fibo_gen(26):
    print(i)

''' Number 7

пишет
нет
модуля
intertools!


from intertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


generator = fibo_gen()
x = 0
for i in generator:
    if x == 15:
        break
else:
    x += 1
    print(f'factorial {x} = {i}'''

'''Number 6

пишет
нет
модуля
intertools!

import intertools

print('Generator Use Enter to continue or q to Stop')
for i in count(int(input('Enter number to start '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Info')
list = input('Info').split()
piter = cycle(list)
quit = None

while quit != "q":
    print(next(piter), end='')
    quit = input()'''

'''Number 5'''

from functools import reduce

list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(lambda a, b: a * b, list))

'''from functools import reduce

def sum_list(el_1, el_2):
    return el_1 * el_2

iq_list = [el for el in range(100, 1001, 2)]
print(f"List {iq_list} Multinumber {reduce(sum_list, iq_list)}")'''

'''Number 4'''

from random import randint

my_list = [randint(-10, 10) for i in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Basic list {my_list} New list {new_list}')

'''Number 3'''

w_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(w_list)

'''Number 2'''

my_list = [2, 4, 1, 6, 9, 33, 7]
one = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1]]
print(one)

'''Number 1'''


def money():
    try:
        hours = int(input('Hours '))
        perhour = int(input('$ per hour '))
        bonus = int(input('Bonus '))
        salary = hours * perhour + bonus
        print(f' Your salary equals {salary}')
    except ValueError:
        return print('This is not a number')


money()
