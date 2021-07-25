from faker import Faker
import  random

#  Функция корекции имени в класс
def correct_name(name) -> str:
    return ''.join(i for i in name if str(i).isalpha() == True) if len(name) > 2 else 'Unkown animal'

# Функция коррекции и проверки целых значений
def correct_natural_value(value) -> int:
    return  value if isinstance(value, int) else random.randint(0, 10000)

# Функция концертации
def transform__value(value) -> float:
    pass
