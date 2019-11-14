''' 5 '''

def summer():
    try:
        with open('file_2.txt', 'w') as f_obj:
            line = input('Enter numbers \n')
            f_obj.writelines(line)
            my_numbers = line.split()
            print(sum(map(int, my_numbers)))
    except ValueError:
        print('Error')
summer()

''' 1'''

f = open('text_1.txt', 'w')
myline = input('Enter info \n')
# f.write('Python1\nPython2\nPython3\nPython4\n')
while myline:
    f.writelines(myline)
    myline = input('Enter info\n')
    if not myline:
        break
f.close
f = open('text_1.txt', 'r')
content = f.readlines()
print(content)
f.close