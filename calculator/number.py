class Number:
    def __init__(self, value):
        if value not in '0123456789':
            raise ValueError

        self.__value = int(value)

    def __add__(self, other):
        return self.__value + self.__value

    def __sub__(self, other):
        return self.__value - self.__value

    def __mul__(self, other):
        return self.__value * self.__value

    def __truediv__(self, other):
        return self.__value / self.__value
