
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


dog = Animal(name='Dog', size=12.6, population ='1m', id=1)

print(dog.info())
