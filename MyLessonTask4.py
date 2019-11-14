def money():
    try:
        hours = int (input('Hours '))
        perhour = int(input('$ per hour '))
        bonus = int(input('Bonus '))
        salary = hours * perhour + bonus
        print(f' Your salary equals {salary}')
    except ValueError:
        return print('This is not a number')
money()