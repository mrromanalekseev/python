print('.............\n.............')
print('------Thank you very much Maria!!!-------')
print('............. 1 .............')


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extr(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def val(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Correct'
                else:
                    return f'Incorrect year'
            else:
                return f'Incorrect month'
        else:
            return f'Incorrect day'

    def __str__(self):
        return f'Data {Data.extr(self.day_month_year)}'


today = Data('21 - 11 - 2019')
print(today)
print(Data.val(22, 11, 2024))
print(today.val(11, 13, 2011))
print(Data.extr('8 - 10 - 2007'))
print(today.extr('21 - 11 - 2019'))
print(Data.val(1, 11, 2000))

print('............. 7 .............')


class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Sum c1 и c2 =')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'* c1 и c2 =')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNum(3, -1)
c_2 = ComplexNum(5, 7)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)

print('............. 456 .............')


class SStore:

    def __init__(self, name, price, quantity, num_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = num_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price per 1': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} Price {self.price} Quantity {self.quantity}'

    def recept(self):

        try:
            unit = input(f'Model ')
            unit_p = int(input(f'Price per 1 '))
            unit_q = int(input(f'Quantity '))
            unique = {'Model': unit, 'Price per 1': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'List -\n {self.my_store}')
        except:
            return f'Incorrect data'

        print(f'Exit - q, Continue - Enter')
        q = input(f'---> ')
        if q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Box -\n {self.my_store_full}')
            return f'Exit'
        else:
            return SStore.recept(self)


class Printer(SStore):
    def to_print(self):
        return f'to print {self.numb} times'


class Scanner(SStore):
    def to_scan(self):
        return f'to scan {self.numb} times'


class Copier(SStore):
    def to_copier(self):
        return f'to copier {self.numb} times'


unit_1 = Printer('China1', 20, 6, 7)
unit_2 = Scanner('China2', 200, 3, 6)
unit_3 = Copier('China3', 10, 2, 4)
print(unit_1.recept())
print(unit_2.recept())
print(unit_3.recept())
print(unit_1.to_print())
print(unit_3.to_copier())

print('------Thank you very much-------')
