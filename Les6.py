'''3'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_personal_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('John', 'Smith', 'Bodyguard', 15000, 5000)
print(a.get_full_name())
print(a.position)
print(a.get_personal_income())


'''2'''

class Road:
    def __init__(self, _length, _width, volume):
        self._length = _length
        self._width = _width
        self.volume = volume

    def mass(self):
        return self._length * self._width * self.volume


r = Road(25, 10000, 125)
print(r.mass())


'''1'''

from time import sleep


class Lights:
    __color = ['Red', 'Yellow', 'Green']

    def run(self):
        i = 0
        while i < 3:
            print(f'Switch \n '
                  f'{Lights.__color[i]}')
            if i == 0:
                sleep(7)
            if i == 1:
                sleep(5)
            if i == 2:
                sleep(3)
            i += 1


Lights = Lights()
Lights.run()
