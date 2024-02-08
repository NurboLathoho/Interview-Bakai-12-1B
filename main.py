'''Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована. 1
Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой. Результат: "AAiddialneat” 1
Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “Money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.'''

# 1)Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

# for i in range(1,6):
#     print(f'{i}: 0')

# 2)Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой. Результат: "AAiddialneat”

# name1 = 'Aidana'
# name2 = 'Adilet'

# mixed_name = ''

# for a1, a2 in zip(name1, name2):
#     mixed_name += a1 + a2

# if len(name1) > len(name2):
#     mixed_name += name1(name2[::-1])
# elif len(name1) > len(name2):
#     mixed_name += name1(name2[::-1])

# print(mixed_name)

# 3)Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.

# baki = 'money, money, money, it’s always sunny, in the richmen’s world'
# print(f'money: {baki.count("money")}')
# print(f"it’s: {baki.count('it’s')}")
# print(f"always: {baki.count('always')}")
# print(f"sunny: {baki.count('sunny')}")
# print(f"in: {baki.count('in')}")
# print(f"the: {baki.count('the')}")
# print(f"richmen’s: {baki.count('richmen’s')}")
# print(f"world: {baki.count('world')}")