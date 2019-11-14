''' задание 5 '''
def my_func():
    sum = 0
    hex = False
    while hex == False:
        a = input('Enter numbers or q for quit - ').split( )
        r = 0
        for el in range(len(a)):
            if a[el] == 'q':
                hex = True
                break
            else:
                r = r + int(a[el])
        sum = sum + r
        print(f'Sum is {sum}')
    print(f'Next sum is {sum}')

my_func()

'''  задаание 4'''

x = int(input('Enter number: '))
y = int(input('Enter number: '))

my_result = pow(x, y)
print(my_result)

'''  задание 3 '''

a = int(input('Enter number: '))
b = int(input('Enter number: '))
c = int(input('Enter number: '))

numbers = [a, b, c]
my_result = sum(numbers) - min(numbers)
print(my_result)

'''  задание 2 '''

var_1 = input('name ')
var_2 = input('surname ')
var_3 = input('date of birth ')
var_4 = input('city ')
var_5 = input('email ')
var_6 = input('phone number ')

print(f'{var_1}, {var_2}, {var_3}, {var_4}, {var_5}, {var_6}')

''' Задание 1 '''

arg_1 = int(input('Enter arg_1 '))
arg_2 = int(input('Enter arg_2 '))

try:
    def my_result(arg_1, arg_2):
        return arg_1 / arg_2


    print(my_result(arg_1, arg_2))

except ZeroDivisionError:
    print('На ноль делить нельзя ')

    ''' Как запускать программу бесконечное количество раз?'''
