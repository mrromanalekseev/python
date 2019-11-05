

'''задание 5'''

my_list = [7, 5, 3, 3, 2]
print(f'Score - {my_list}')
digits = int(input("Enter numbers between 0 and 100 - выход) "))
while digits != 100:
    for el in range(len(my_list)):
        if my_list[el] == digits:
            my_list.insert(el + 1, digits)
            break
        elif my_list[0] < digits:
            my_list.insert(0, digits)
        elif my_list[-1] > digits:
            my_list.append(digits)
        elif my_list[el] > digits and my_list[el + 1] < digits:
            my_list.insert(el + 1, digits)
    print(f' - {my_list}')
    digit = int(input('Enter number '))


''' задание 4 '''

my_string = input('Enter words ').split( )
for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')

''' задание 3 '''

sns_list = ['winter', 'spring', 'summer', 'autumn']
sns_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
months = int(input('Enter number of the month'))
if months == 1 or months == 12 or months == 2:
        print(sns_dict.get(1))
        print(sns_list[0])
elif months == 3 or months == 4 or months == 5:
    print(sns_dict.get(2))
    print(sns_list[1])
elif months == 6 or months == 7 or months == 8:
    print(sns_dict.get(3))
    print(sns_list[2])
elif months == 9 or months == 10 or months == 11:
    print(sns_dict.get(4))
    print(sns_list[3])
else:
    print("No such month")

'''задание 2'''

x = int(input("Enter number of Elements "))
print(f'{x} elements')
my_list = []
i = 0
el = 0
while i < x:
    my_list.append(input("Enter element "))
    i += 1

for elements in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

'''задание 1'''

my_list = [-15, False, 100, 'Girls', 100.5,[1, 2], (14, 18)]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)