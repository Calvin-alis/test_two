from utilits import  correct_name
from utilits import correct_natural_value

class Animal:

    # Инициализатор с 4 полями
    def __init__(self, name, size, population, id):
        self.name = name
        self.size = size
        self.population = population
        self.id = id

    # Фукнция вывода всей информации
    def info(self):
        return f' Name of animal : {self.name}\n Mean size of animal : {self.size}\n Population : {self.population}\n Unique id : {self.id}'

    # Функция проверки на тип данных
    def chech_out(self):
        return correct_natural_value(self)


dog = Animal(name='Dog', size=12, population = 10**4, id=1)

cat = Animal(name='Cat', size= 5, population= 10**5, id=1)

print(Animal.chech_out(cat.id))
