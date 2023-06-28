name: str = input('Введите ваше имя:')
age: int = int(input('Введите ваш возраст:'))

greeting: str = 'Привет, ' + name + '! Тебе уже ' + str(age) + '!'

print(greeting)
