# ------------------------------------1-----------------------------
'''
������� ����� TrafficLight (��������) � ���������� � ����
���� ������� color (����) � ����� running (������).
������� ����������� ��� ���������.
� ������ ������ ����������� ������������ ��������� � ������
�������, ������, �������.
����������������� ������� ��������� (�������) ���������� 7 ������,
������� (������) � 2 �������, �������� (�������) �
�� ���� ����������.
������������ ����� �������� ������ �������������� ������
� ��������� ������� (�������, ������, �������).
��������� ������ �������, ������ ��������� � ������ ��������� �����.
������ ����� ���������, ���������� �������� ������� �������,
� ��� ��� ��������� �������� ��������������� ��������� �
��������� ������.
'''

from time import sleep


class TrafficLight
    __color = ['�������', '������', '�������']

    def running(self)
        i = 0
        while i  3
            print(f'�������� ������������� n '
                  f'{TrafficLight.__color[i]}')
            if i == 0
                sleep(7)
            elif i == 1
                sleep(5)
            elif i == 2
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

'''
# ------------------------------------2-----------------------------
����������� ����� Road (������), � ������� ���������� ��������
length (�����), width (������).
�������� ������ ��������� ������ ������������ ��� ��������
���������� ������. �������� ������� �����������.
���������� ����� ������� ����� ��������, ������������
��� �������� ����� ��������� �������.
������������ ������� ���������������� ��������
��� �������� ������ �� ����� ������ ���������, ��������
� 1 ������� �� ������� �������. ��������� ������ ������.
�������� 20�5000�25��5�� = 12500 �
'''


class Road
    def __init__(self, _length, _width)
        self._length = _length
        self._width = _width

    def mass(self)
        return self._length  self._width


class MassCount(Road)
    def __init__(self, _length, _width, volume)
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(25, 10000, 125)
print(r.mass())

'''
# ------------------------------------3-----------------------------
����������� ������� ����� Worker (��������), � ������� ����������
�������� name, surname, position (���������), income (�����).
��������� ������� ������ ���� ���������� � ��������� �� �������,
���������� �������� ����� � ������, ��������,
{wage wage, bonus bonus}. ������� ����� Position
(���������) �� ���� ������ Worker.
� ������ Position ����������� ������ ��������� �������
����� ���������� (get_full_name) � ������ � ������ ������
(get_total_income). ��������� ������ ������� ��
�������� ������ (������� ���������� ������ Position,
�������� ������, ��������� �������� ���������, �������
������ �����������).
'''


class Worker

    def __init__(self, name, surname, position, wage, bonus)
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {wage wage, bonus bonus}


class Position(Worker)

    def __init__(self, name, surname, position, wage, bonus)
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self)
        return self.name + ' ' + self.surname

    def get_total_income(self)
        return self._income.get('wage') + self._income.get('bonus')
        # return f'{sum(self._income.values())}'


a = Position('Peter', 'The Great', 'Beekeeper', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

'''
# ------------------------------------4-----------------------------
���������� ������� ����� Car. � ������� ������ ������ ����
��������� �������� speed, color, name, is_police (������).
� ����� ������ go, stop, turn(direction), ������� ������
��������, ��� ������ �������, ������������, ��������� (����).
������� ��������� �������� ������� TownCar, SportCar, WorkCar,
PoliceCar. �������� � ������� ����� ����� show_speed, �������
������ ���������� ������� �������� ����������. ��� ������� TownCar
� WorkCar �������������� ����� show_speed.
��� �������� �������� ����� 60 (TownCar) � 40 (WorkCar)
������ ���������� ��������� � ���������� ��������.
�������� ���������� �������, ��������� �������� ���������.
��������� ������ � ���������, �������� ���������.
��������� ����� ������� � ����� �������� ���������.
'''


class Car
    # atributes
    def __init__(self, speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self)
        return f'{self.name} is started'

    def stop(self)
        return f'{self.name} is stopped'

    def turn_right(self)
        return f'{self.name} is turned right'

    def turn_left(self)
        return f'{self.name} is turned left'

    def show_speed(self)
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car)
    def __init__(self, speed, color, name, is_police)
        super().__init__(speed, color, name, is_police)

    def show_speed(self)
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed  40
            return f'Speed of {self.name} is higher than allow for town car'
        else
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car)
    def __init__(self, speed, color, name, is_police)
        super().__init__(speed, color, name, is_police)


class WorkCar(Car)
    def __init__(self, speed, color, name, is_police)
        super().__init__(speed, color, name, is_police)

    def show_speed(self)
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed  60
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car)
    def __init__(self, speed, color, name, is_police)
        super().__init__(speed, color, name, is_police)

    def police(self)
        if self.is_police
            return f'{self.name} is from police department'
        else
            return f'{self.name} is not from police department'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.turn_left())
print(f'When {oka.turn_right()}, then {audi.stop()}')
print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {audi.name} a police car {audi.is_police}')
print(f'Is {lada.name}  a police car {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())

'''
# ------------------------------------5-----------------------------
����������� ����� Stationery (������������ ��������������).
���������� � ��� ������� title (��������) � ����� draw (���������).
����� ������� ��������� ������� ���������.�
������� ��� �������� ������ Pen (�����), Pencil (��������),
Handle (������). � ������ �� ������� �����������
��������������� ������ draw. ��� ������� �� �������
������ ������ �������� ���������� ���������.
������� ���������� ������� � ���������, ��� �������
��������� ����� ��� ������� ����������.
'''


class Stationary
    def __init__(self, title)
        self.title = title

    def draw(self)
        return f'������ ��������� {self.title}'


class Pen(Stationary)
    def __init__(self, title)
        super().__init__(title)

    def draw(self)
        return f'�� ����� {self.title}. ������ ��������� ������'


class Pencil(Stationary)
    def __init__(self, title)
        super().__init__(title)

    def draw(self)
        return f'�� ����� {self.title}. ������ ��������� ����������'


class Handle(Stationary)
    def __init__(self, title)
        super().__init__(title)

    def draw(self)
        return f'�� ����� {self.title}. ������ ��������� ��������'


pen = Pen('�����')
pencil = Pencil('��������')
handle = Handle('������')
print(pen.draw())
print(pencil.draw())
print(handle.draw())