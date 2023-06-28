working_hours: float = float(
    input('Введите количество отработанных часов в месяц: '))

hourly_rate: int = 22 * 8

salary: float = hourly_rate * working_hours

print('Ваша почасовая ставка:', hourly_rate, 'рублей')
print('Заработная плата в месяц:', salary, 'рублей')
