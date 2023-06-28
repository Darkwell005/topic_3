name: str = input('Введите ваше имя:')
surname: str = input('Введите ваше фамилию:')
age: int = int(input('Введите ваш возраст:'))

print('Тип имени: ', type(name), ', ID в памяти: ', id(name), sep='')
print('Тип фамилии: ', type(surname), ', ID в памяти: ', id(surname), sep='')
print('Тип возраста: ', type(age), ', ID в памяти: ', id(age), sep='')
