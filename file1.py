# Тип данных словаки (dict) 

# словари - это одна из наиболее часто используемых структук данных, позволяющий хранить обекты
# словарь - изменяемый, итерируемый, неиндуксируемый, упорядоченный тип данных в котором элементы храняться в виде пары ключ значение


# {} - литералы

# dct = {}
# print(type(dct))

# dict_ = {'a': 'hello', 'b':2, 'c':3}

# dict_ = {{'s':5}:5} - None
# print(dict_)

# dict1 = {1:'hello', 2:[1,2,3,4], 4.5:{'a':2}, (1,2,3): 'a'}
# print(dict1[1])

# dct = {'name': 'Jown', 'age': 25, 'hobby': ['fishing', 'footbal', 'dota'] }

# print(dct['hobby'])
# print(dct['hobby'][1])
# data = {'email': 'john@gmail.com', 'password': 'im1m2m333'}

# dict2 = dict([('key1', 'value1'), ('key2', 'value2')])
# print(dict2)

# dict3 = dict(['ab', 'cd','de'])
# print(dict3)


# dict4 = dict()
# dict4['key1'] = 'value1'
# print(dict4)


# dct = dict(age=25)
# print(dct)
# dct['age'] = 23
# print(dct)


# dct = {'age': True, 'age': 78}
# print(dct)


# dict.clear() - очищает словать

# dct = {'name': 'john', 'age': 25}
# dct.clear()
# print(dct)


# import copy

# copy() - возвращает копию словаря

# dct = {'name': 'Ryu', 'age': 18, 'hoppy': ['game', 'anime', 'diving']}
# dct2 = dct.copy()
# dct2['hoppy'][2] = 'hi'
# print(dct2)


# fromkeys[object, value] - создает словать с ключами из object и значием value для всех ключей если не передать value то значение у всех ключей будет None 

# list1 = ['name', 'age', 'hobby']
# dct = dict.fromkeys(list1, 'hi')
# print(dct)

# d = dict.fromkeys('a')
# print(d)

# методы получения элементов словаря

# get(key, default) - возвращает значение по этому ключу

# dct = {'name': 'Ryu', 'age':18}
# print(dct.get('age', 'нет такого ключа'))  # -- выдает None если нет такого ключа
# print(dct['age']) # -- выдает ошибку если такого ключа тен


# update - добавляет новый словарь в наш словарь

# dct = {'name': 'Jack', 'age': 18}
# new_dct = {'hobby': ['game', 'anime']}
# dct.update(new_dct)
# print(dct)


# setdefault - получение значений, работает точно также как get() но если такого ключа нет он создаст новую пару

# dct = {'name': 'Ryu', 'age': 18}
# dct.setdefault('hobby')
# print(dct)


# values() - выводит значение которое есть в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.values()))


# keys() - выводит ключи которые есть в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.keys()))


# items() - выводит все ключи и значение в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.items()))


# pop(key, [message]) - удалет пару ключи и значение и возвращает значениею. если ключа нет то возвращает message (по умаолчанию приходит ошибка)


# dct = {'name': 'Ryu', 'age': 18}
# remove = dct.pop('name')
# print(remove)
# print(dct)


# popitem()  - удаляет и возвращает пару ключ значение удаляет последнюю добавленную пару

# dct = {'name': 'Ryu', 'age': 18}
# # dct['address'] = 'Bischkek'
# remove = dct.popitem()
# print(remove)

# ============================ Задачки =======================

# ==========================1

# dict_ = {'a': 1, 'b': 2, 'c': 3, 'e': 4, 'd': 5, 'y': 6}

# for key,value in dict_.items():

#     if value%2==0:
#         dict_[key] = 0
        

# print(dict_)


# =========================2

# dict_ = {'hello': None, 'python': None, 'javascript': None, 'makers': None}

# for keyl in dict_.keys():
#     dict_[key] = len(keyl)

# print(dict_)


# ========================3

# dict_ = {'John': 60, 'Jack': 70, 'Anton': 85, 'Bake': 81, 'Nastya': 93}

# nums = 0
# for num in dict_.values():
#     nums += num

# number = nums / len(dict_)
# dict_['avarage'] = number
# print(dict_)        



# ====================== tasks 24 avgust

# ====================1

# university = {'программирование': 99, 'экономика': 50, 'медицина': 78}


# university['программирование'] = 23
# univer = {'лингвистика': 87}
# university.update(univer)
# university.pop('медицина')

# print(university)

# sumn = 0
# summ = []
# for i in university.values():
#     sumn += int(i)
    

# print(f'Колв учатнищихся: {sumn}')


# =======================2


# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# dict_swapped = {
# value: key

# for key,value in dict_.items()

# }

# print(dict_swapped)


# ======================3


# gest = int(input('Введите количество гостей которых хотите пригласить: '))

# gests = {}
# number = 0

# while True:
#     number +=1
#     gest1 = input('По одному введите имя гостей которые придут: ')
#     gests[number] = gest1
    
#     if len(gests) == gest: break


# print(gests)



# ========================4



# baylist = {1:'Помидор', 2:'Огурец', 3:'Молоко', 4:'Кефир', 5:'Банан'}

# print(f'Мне нужно купить: {baylist}')

# bayll = len(baylist)

# number = 0
# while len(baylist) != 0:

#     bayed = input("Я купил: ")
#     number += 1
#     if number == 5: break
#     for key,value in baylist.items():
#         if value == bayed:
#             baylist[key] = 0
            
        
        

# print(f'Пора расплататься в кассе Xd')

# for key,value in dict_.items():

#     if value%2==0:
#         dict_[key] = 0
        


# Задание 9
# Создайте словарь a с числовыми значениями. Создайте новый словарь b, такой же как словарь а, но все четные значения замените на 2.

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {} 
# for k, v in a.items(): 
#     if v%2==0: 
#         b.setdefault(k, 2) 
#     else: 
#         b.setdefault(k,v) 
# print(b)




# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# c = {} 
# for k, v in a.items(): 
#     b = v / 5 
#     c.setdefault(k,b) 
# print(c)



# Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным (специальным методом) и распечатайте результат.

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()): 
#     if v % 2 == 0: 
#         del a[k] 
# print(a)



# В переменные a1 , a2 , a3 создайте любые словари тремя возможными способами.

# a1=dict(a=1, b=2, c=3) 
# a2=dict([('d', 4),('e', 5),('f', 6)]) 
# a3=dict([('a', 1)], b=2, c=3) 
# a4=dict({'a' : 1, 'b' : 2}, c=3) 
# print(a1) 
# print(a2) 
# print(a3) 
# print(a4)



# Дан словарь dict1, где ключами будут цены товаров, а значениями их названия, затем пройдитесь циклом по нему и поменяйте все ключи элементов, возведя их в квадрат, новые элементы запишите в словарь dict2

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}

# for k,v in dict1.items(): 
#     dict2.setdefault(k**2,v) 
# print(dict2)




# Из предыдущего словаря dict_, достаньте ключ, значение которого является максимальным, если значений несколько, распечатайте каждый из них по отдельности.

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}

# mm = max(dict_.values())
# for k in dict_.keys():
#     if dict_[k] == mm:
#         print(k)




# Дан словарь dict_, значениями, которого являются словари, измените словарь dict_ таким образом, чтобы значения внутреннего словаря стали внешними значениями

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

# for k,v in list(dict_.items()): 
#     for v2 in v.values(): 
#         dict_[k] = v2 
# print(dict_)


# Дан словарь dict1. Создайте словарь dict2, с ключами как в словаре dict1, а значениями пусть будут произведение чисел внутренних словарей

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}

# for k,v in list(dict1.items()): 
#     res = 1 
#     for j in v.values(): 
#         res = res * j 
#         dict2[k] = res 
# print(dict2)




# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}

# for i in int(list_):
#     if i.isalpha():
#         k = i
#         dict_.setdefault(k,v)
#     elif i%2:
#         v = i
#         dict_.setdefault(k,v)
    
# print(dict_)



# Дан список, состоящий из строк и чисел. Создайте словарь, ключами которого будут строки из списка, а значениями числа

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding'] 

# ls = [x for x in list_ if type(x)==int] 
# ls2 = [x for x in list_ if type(x)==str] 
# dict_ = dict(zip(ls2, ls)) 
# print(dict_)





# Дан словарь dict_. Отсортируйте словарь по значениям в порядке увеличения.
# Новые элементы занесите в словарь sorted_dict

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# sorted_dict = {k:item for item in sorted(dict_.values()) 
# for k,v in dict_.items()
#     if item == v} 
# print(sorted_dict)



# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {k:item 
# for item in sorted(dict_.values(), reverse=True) 
# for k,v in dict_.items() 
# if item == v} 
# print(sorted_dict)




# Дан словарь. Найдите сумму значений словаря, который хранится под ключом vars, используя значение словаря, под ключом math

# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }

# res = dict_.get('vars')

# for k,v in dict_.items():
#     for j in v.values():
#         if type(j) != int:

#             print(j(res.values()))





# a = {'a': 10, 'b': 9, 'c': 3}

# result = 1 

# for k, v in a.items():
    
#     result *= v
    
# print(result)



# нужно создать новый словарь, ключами которого будут буквы строки, а значениями числа, соответствующие количеству повторений данной буквы в строке.

# string = "pythonist" 

# dict_ = {}
# for i in string:
#     lenn = string.count(i)
#     dict_.setdefault(i,lenn)
# print(dict_)





# цикл for позволяет пройтись по каждому элементу итерируемого объекта

# name = 'John'

# for letter in name:
#     print(letter)


# '''
# Синтаксис:

# name = 'john'

# for <var_name> in name:
#     pass

# '''

# # ================= Условные операторы

# money = 100

# if money > 100:
#     print('Покупаю 2л колу')  
# elif money == 0:
#     print('I will have to still')
# else:
#     print('Покупаю кефир')

# '''
# Синтакис:

# if < Условие1 >:
#     pass
# elif < Условие2 >:
#     pass
# else:
#     pass
# '''

# x = 87
# y = 23

# resolt = x / y

# if x / y:
#     print(f'Частное: {resolt}')

# Задание 8
# В переменные x, y попадают числа вводимые пользователем. Проверить делится ли первое число на второе без остатка.

# x = int(input()) 
# y = int(input()) 
# if x % y == 0: 
#     print('x делится на y') 
#     d = x//y 
#     print(f'Частное: {d}') 
# else: 
#     print('x не делится на y') 
#     a = x // y 
#     print(f'Частное: {a}') 
#     b = x % y 
#     print(f'Остаток: {b}')


# Задание 9
# В переменную year попадает число-год от пользователя.
# Определите, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.

# year = int(input())

# if year%4 == 0 and year%100 != 0 : 
#     print('YES') 
# elif year%400 == 0: 
#     print('YES') 
# else: 
#     print('NO')

# string = '123214'
# print(string[3:6])
# print(string[0:3])

# Логические выражения и операторы


#  boolen

# pritn(bool(0))
# bool(3)
# bool(-233)
# bool('hello')
# bool(' ')
# bool('') False

# a = 3
# == --> bool
# print(int('2' == 2))

# != - не равно

# print( 5 != 5) - False 
# print( 2 != 3) - True 

# > < -- bool 


# Логические операторы

# and - голическое и
# or - логическое или
# not - логическое отрицание

# a = 5
# b = 6

# print(a == 5 and b == 6) - True 
# a == 3 and b == 3 - False 

# print(a == 5 or b == 7)

# print(not True)
# print(not False)
# not a == 5 - False 
# not a == 4 - True 

# Оператор индетификации

# in - > проверяет наличие элемента

# сравнивание

# == - сравнение по значению 
# is - сравнение по ячейкам памяти


# str_ = 'hello'

# if 'e' in str_:
#     print('worked')


# a = [1, 2, 3]
# b = [1, 2, 3]

# print(id(a))
# print(id(b))
# print(a is b) - False
# print(a == b) - True

# bool('None')
# bool(None)

# a = None 
# print(a is None)



# Условные операторы - нужны для того, чтобы при разных входных данных код работал по разному


# if a:
#     print('worked')

# age = int(input('Введите ваш возраст:'))

# if age >=18:
#     print('Доступ разрещен!')
# elif age <= 17:
#     print('в Доступе отказана')


# number = int(input('Ввидите число:'))

# if number % 2 == 0:
#     print('ch')
# else:
#     print('no')

# import random

# num = int(input('Ввидите число от 1 до 5: '))

# numm = random.randint(1, 5)

# if num == numm:
#     print('Вы угадали число')
# else:
#     print('Вы не угадали число')


# handu = input('Ваш выбор: ')

# handb = random.randint('Камень', 'Ножницы', 'Бумага')

# if 'Камень' in handu and 'Ножницы' in handb:
#     print('Ваш выбор: Камень')
#     print('Выбор компьтера: Ножницы')
#     print('Вы выиграли!')
# elif 'Ножницы' in handu and 'Бумага' in handb:
#     print('Ваш выбор: Ножницы')
#     print('Выбор компьтера: Бумага')
#     print('Вы выиграли!')
# elif 'Бумага' in handu and 'Камень' in handb:
#     print('Ваш выбор: Бумага')
#     print('Выбор компьтера: Камень')
#     print('Вы выиграли!')
# elif 'Камень' in handu and 'Камень' in handb:
#     print('Ваш выбор: Камень')
#     print('Выбор компьтера: Камень')
#     print('У вас Ничья!')
# elif 'Ножницы' in handu and 'Ножницы' in handb:
#     print('Ваш выбор: Ножницы')
#     print('Выбор компьтера: Ножницы')
#     print('У вас Ничья!')
# elif 'Бумага' in handu and 'Бумага' in handb:
#     print('Ваш выбор: Бумага')
#     print('Выбор компьтера: Бумага')
#     print('У вас Ничья!')
# elif 'Камень' in handu and 'Бумага' in handb:
#     print('Ваш выбор: Камень')
#     print('Выбор компьтера: Бумага')
#     print('Вы Проиграли!')
# elif 'Бумага' in handu and 'Ножницы' in handb:
#     print('Ваш выбор: Бумага')
#     print('Выбор компьтера: Ножницы')
#     print('Вы Проиграли!')
# elif 'Ножницы' in handu and 'Камень' in handb:
#     print('Ваш выбор: Ножницы')
#     print('Выбор компьтера: Камень')
#     print('Вы Проиграли!')
# тернарные операторы это условие в одну строку

# тела1 if условие else тело2
# a = 5
# res = 'Hello' if a == 4 else 'Bye'

# маржовые операторы позволяет нам как присваивать значение переменной, так и  возвращает ее значение

# print(num = 15)
# print(num := 15)
# print(num)

# operator = input('Введите необходимый оператор:(+, -, *, /,)')
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))

# if operator == '+':
#     print(number1 + number2)



# FizzBuzz

# num = input('Введите имя: ')
# num1 = int(input('Сколько у вас друзей? '))


# name = 'друзей'
# name1 = 'друг'

# if num1 > 1 or num1 == 0:
#     print(f'У {num} {num1} {name}!')
# elif num1 <= 1:
#     print(f'У {num} {num1} {name1}')


# if num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0 and num % 3 == 0:
#     print('FizzBuzz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print(num)

# num = int(input('Введите число1: '))
# num1 = int(input('Введите число2: '))
# num2 = int(input('Введите число3: '))

# if num==num1==num2==num:
#     print('Равносторонний треугольник!')
# elif num==num1!=num2:
#     print('Равнобедренный треугольник!')
# elif num!
# num*num1 == 90 or num*num2 ==90 or num1*num2==90:


# password = input('Введите парель: ')

# if  password.isdigit() and len(password) >= 8:
#     print('Ваш пароль сохранен!')
# elif password.isalpha() :
#     print('Ваш пароль должен хранить только числа!')

# if len(password) <= 7:
#     print('Ваш пароль должен содержать не менее 8 символов')

# bal = input("Введите свои баллы по математике, английскому языку и литературе через запятую: ")

# ball = bal.replace(',','')

# ball1 = ball.split()

# resb = int((ball1[0] + ball1[1] + ball1[2]) / 2)

# if resb >= 70:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {resb}')
# elif resb <=69:
#     print(f'У вас недопуск с экзаменам. Ваш средний балл составляет {resb}')

# string = 'RyuDzaky'

# print(string[-1])
# print(string[-2:])
# print(string[::-1])
# print(len(string))

# string = 'The quick brown fox jumps over the lazy dog'

# print(string.replace('o','*'))

# usser = input("Введите имя, фамилию, возраст и город, в котором вы проживаете: ")
# name =  usser.split()
# namef = name[0]
# names = name[1]
# age = name[2]
# city = name[3]
# print(f'Вас зовут {namef} {names}, Ваш возраст: {age}, Вы проживаете в городе {city}')


# number = int(input('Введите число: '))

# if number > 5:
#     print('True')
# elif number < 5:
#     print('False')







# print('Hello world')

#коментании

"""
видты коментариев
ctrl+/
cmnd+/
коментарии
"""

# 1. NoneType -> ничего (None)
# 2. Boolean -> Правда или Ложь (True/False)
# 3. Числовые тыпы данных
# a. integer -> целое число 1, 10, 5, 9,
# b. float - число с плавающей точкой (1.23, 3.59)
# c. complex - комплексные числа (2+3i/j)
# 4. Списковые типы танных

# a. list() массив -> [1,2,3,4,5,6, None, 'asdas', {'1': 'a'}]

# b. tuple() Кортеж -> (1,2,3,4,5,6, True, False)

# 5. string
# Строки -> 'Hello world', 'Python3', '123'

# 6. set() -> Множество -{1,2,3,4,5,6, None, False, True, True}

# 7. frosenset() - замороженное множество {1,2,3,4,5,6, None, False, True, True}


# dict() -> словарь содержит данные в виде пары ключ/значение

# {1;'a'} {'id': 1} {'usermane': 'atai'} {'password': 1234123412341234}


# Неизменяемыые типы данных
# 1.NoneType
# 2.Boolean
# 3.int()
# 4.float()
# 5.complex()
# 6.tuple()
# 7.str()
# 8.frozenset()


# Изменяемые типы данных
# 1.list()
# 2.set()
# 3.dict()



'================Переменные================'

# Переменная = это ссылка на ячейку памяти в которой хранится какая то информация 
# В переменной мы можем хранить разные типы данных

# a = 4 

# как должны называться

# Название переменной в Python должно начинаться с алфавитного символа или со знака нижнего подчеркивания

# a = 1
# x = 2
# _x = 3

# age1 = 1

# age_3 = 4

# имя не может начинаться с цифры

# имя не может содержать символы = @ $ %

# age% = 2 нельзя


# Нельзя использовать зарезервированные слова

# if else for while

# int()
# str()
# list()


# number = int()
# string = str()
# list_of_numbers = list()
# print(number)
# print(string)
# print(list_of_numbers)


# Python является языком с динамической типизацией

# int number = 2 c#

# Диинамическая типизация
# number = '1'
# number = 1
# number = []


'======================Ввод и вывод данных======================'


# number = int(input('Введите число')) #ввод от пользователя возвращает всегда в строке str
# print(type(number)) #type - функция которая выводит тим данных
# print('Введенное число', number)

# string = '1'
# print(type(string))
# print(int(string) + 1)

'=====================Операция над числами========================='

# '+' - сложение
# a = 10
# b = 5
# result = a + b
# print(result)
# print(a+b)

# '/' = деление

# 5 / 2 = 2.5 --- float()
# print(int(5 / 2))

# '//' - целочисленое деление

# a = 5
# b = 2
# print(a // b)

# 5 / 2 = 2.5
# 5 // 2 = 2 -- оставляет только целое число

# '*' умножение

# print(5 * 2)

# % - остаток от деления при котором мы получаем остаток

# a = 2
# b = 4
# print(a % b)

# '**' - возведение в степень

# print(5 ** 2)

# 25 ** 0.5 - квадратные корень числа

# модуль числа - из отрицаательного в положительное

# abs(-5) # 5
# abs(5) # 5
# abs(-2.4) # 2.4

# pow()
# 1. возводит в степень
# 2. возвращает остаток от деления(результат первых двух чисел трете)


# print(pow(2,3)) 2 ** 3
# print(pow(2,3,4)) (2 ** 3) % 4

# print(pow(2,3,4))

# divmod - функция которая принимает 2 числа и возвращает 2 числа
# 1. результат целочисленного деления //
# 2. остаток от деления %
# divmod(2,3) # 2//3, 2%3

# print(divmod(2,3))

# round - футкция которая округляет число

# round(5.6) 6
# round(3.5) 4
# round(4.4) 4
# print(round(7.49, 2))

# можно показать сколько цифр после запятой оставить

# print(round(10.0475, 3))

# from math import pi

# # math.py
# pi = 23.23
# from integer import a

# print(pi)

# print(round(pi, 3))


# import math
# dir() - возвращает функции модуля или файла
# print(dir(math))


# from math import sqrt, pi
# import math

# sqrt - функция для нахождения корня числа

# print(sqrt/или/math(36))

# множественное присваивание

# x = 1
# y = 2
# z = 3
# print(x)

# x = y
# y = z
# z = x
# print(x)

# x,y,z = y,z,x

# Дана переменная с радиусом окружности, найдите периметр и площадь окружности, результат выведите в терминал.
# S = pi * r2,
# C = 2 * pi * r.

# from math import pi

# r = int(imput('Введите радиус:  '))

# result_S = pi * (r ** 2)
# result_P = 2 * pi * r







# bool - булевый класс или тип данных

# a = True
# print(type(a))

# b = False
# print(type(b))


# print(int(True))
# print(int(False))


# # Здесь работает правило: все, что не 0 или не пустота, является правдой
# print(bool(3.4))
# print(bool(-150))
# print(bool(0))
# print(bool(' '))
# print(bool(''))



# ===================Присваивание и сравнение - разрые операции===================

# a = 10
# b = 5

# print(a + b > 14)
# print(a < 14 - b)
# print(a <= b + 5)
# print(a != b)
# print(a == b)
# c = a == b
# print(a, b, c,)




# x = 8
# y = 13 
# print(y < 15 and x > 8) # False  




# print(y < 15 or x > 8) # True  



# print(not y < 15) # False  




# a = 5 
# b = 0 
# print(not a) # False  
# print(not b) # True  


# цикл for позволяет пройтись по каждому элементу итерируемого объекта

# name = 'John'

# for letter in name:
#     print(letter)


# '''
# Синтаксис:

# name = 'john'

# for <var_name> in name:
#     pass

# '''

# # ================= Условные операторы

# money = 100

# if money > 100:
#     print('Покупаю 2л колу')  
# elif money == 0:
#     print('I will have to still')
# else:
#     print('Покупаю кефир')

# '''
# Синтакис:

# if < Условие1 >:
#     pass
# elif < Условие2 >:
#     pass
# else:
#     pass
# '''

# # if логическое_выражение: 
# #     выражение 1 
# #     выражение 2




# if n < 100: 
#     b = n + a 




# b = 0 
# a = 50 
# n = 98 
# if n < 100:
#     b = n + a 
# print(b) 




# # if логическое_выражение:
# #     выражение 1
# #     выражение 2
# # else:
# #     выражение 3 




# tovar1 = 50 
# tovar2 = 32 
# if tovar1 + tovar2 > 99: 
#     print("99$ недостаточно") 
# else: 
#     print("Чек оплачен") 




# a = 5 > 0 
# if a: 
#     print(a)
# if a > 0 and a < b: 
#     print(b - a) 




# user_is_logged_in = True 
# user_has_facebook_account = True 
# user_has_github_account = True 
# if user_is_logged_in: 
#     print("Logged in") 
# if user_has_facebook_account: 
#     print("Has FB account") 
# if user_has_github_account: 
#     print("Has Github account")




# user_is_logged_in = True 
# user_has_facebook_account = False 
# user_has_github_account = True 
# if user_is_logged_in: 
#     print("Logged in") 
# elif user_has_facebook_account: 
#     print("Has FB account") 
# elif user_has_github_account: 
#     print("Has Github account") 
# else: 
#     print("Not logged in and has no accounts")






# строки - неизменяемый тим данных  который предназначен для хранения текста
# заключаются в одинарные и двойные ковычки

# string1 = 'строка с одиранрыми ковычками'
# string2 = "стора с двойными кавычками"
# error = "Dont't do it'
# string3 = "Don't"
# string4 = "Makers"

# print(string4)

# string = ''''''
# текст '""'""'"'"
# ''' тут можно ставить любые ковычки

# print('Hello\nworld') - перенос на следующую строку
# print('Hello\n\tworld') - перенос по табуляции

# while True:
    # string = '1'



# =========Конкатенация (сложение)============

# S1 = 'spam'
# S2 = 'eggs'

# print(S1 + S2)

# # ============Дублирование строки===============

# print('spam' * 3)

# # ===============Длина строки (функция len)=================

# len('spam')

# # ================Доступ по индексу==================

# S = 'spasm'

# print(S[0])

# # =================Извлечение среза===================

# s = 'spameggs'

# print(s[3])

# print(s[2:-2])

# print(s[::-1])

# print(s[3:5:-1])

# print(s[2::2])



# # ======================Форматирование строк=======================

# # format() - возвращает отформатированную версию строки, заменяя идентификаторы в фигурных скобках. Идентификаторы могут быть позиционными, числовыми индексами, ключами словарей, именами переменных.

# name = 'Steve'
# hello = 'Hello, {}'.format(name)

# print(hello)

# # f'string - внутри f'строки в паре фигурных скобок укказываются имена переменных, которые надо подставить:

# namee = 'John'
# surname = 'Snow'

# print(f"{namee},{surname}")

# # % - Структура данных типа форматирования выглядит так:

# print('Hellj, %s!' % 'Vasya')


# Методы типов данных - функции, к которым мы обращаемся через точку



# Методы на is 

# все что начинается на is  возвращает True/False 

# string = 'hello world'

# isdigit() - возвращает True если строка полностью состоит из цифр

# print(string.isdigit())


# isalpha() - возвращает True если строка полностью состоит из букв

# print(string.isapha())


# isalnum() - состоит ли строка из цифр или букв

# string = 'Ryu8998'
# print(string.isalnum())  # --- False


# islower() - состоит ли строка из символов в нижнем регистре

# print(string.islower())


# isupper() - состоит ли строка из символов в верхнем регистре

# isspase() - состоит ли строка из неотображаемых символов

# istitle() - начинаются ли слова в строке с заглавной буквы

# print(string.istitle())


# print(dir(str)) посмотреть все методы типа данных


# lower() - переводит целую строку в нижний регистр

# print('HELLO'.lower())


# upper() - переводит целую строку в верхний регистр

# print('sdkjlj'.upper())


# swapcase() - переводит символы в противоположный регистр

# print('Hello World'.swapcase())


# title() - переводит каждую букву слова в строке в верхний регистр

# print('hello world'.title())


# strip() - убирает пробелы в начале и в конце строки

# print('    Hellow     '.strip())


# lstrip() rstrip() - убирает слева или справа


# replace() - меняет местами или заменяет

# print('hsaap'.replace('hsaap', 'sheep' 1))


# split() - делит стоку по разделителю и возвращает массив list() 

# print('You Are'.split())


# индекс - порядковый номер символа в строке

# 'hello world'

# # h e l l o  w o r l d
# # 0 1 2 3 4 5 6 7 8 9 10



# : - подстрока строки СРЕЗЫ
# string[start:end:step]


# string = 'hello world'
# print(string[0:5])
# print(string[0:6])
# print(string[:])
# print(string[0:5][2:4][:1])
# print(string[6:])
# print(string[:11:2])
# print(string[::3])
# print(string[::-1])


# capitalize() - переводит первый символ в верхний регистр

# print('hello'.capitalize())


# endswith(element) возвращает True если строка заканчивается на element

# print('hello world'.endswith('!'))


# startswith(element) - возвращает True если строка начется на element

# print('makers'.startswith('k',2))


# count(element) - считает количество вхождений element в строке

# print('makers'.count())


# len() - считает длину строк

# print(len(dude))


# index()

# print('hello'.index('l'))

# indexs = 'hello'.index('o')
# print(indexs)

# find()

# print('lello'.find('l'))


# id()

# a = 'hello'
# print(id(a))


# join() - применяет в себя список

# text = "Milk, Bread, Water"

# text = "Snow"
# split = list(text)
# print(split)

# joined = "*".join(split)
# print(joined)

# text = 'coder'

# print(text[-1] + text[1:4])

# address = '1.1.1.1'

# print(address.replace('.', '[.]'))

# Вывод фамилию с инициалами;

# name = input('Введите свое имя:')

# you = name.split()

# your_in = you[0].capitalize() + ' ' +you[1][0].capitalize() +' ' + you[2][0].capitalize()

# print(your_in)


# ========Проверка слов в if============

# res = input('Ввидите слово:')

# # if res.find('сок') != -1: <> выводит индекс

# if 'сок' in res:
#     print(True)
# else:
#     print(False)



# res = input('Введите имя, фамилия и возраст через пробел:')

# res0 = res.split()

# res2 = res0[0].replace('a','')
# res1 = list(res0[1])
# res11 = "*".join(res1)
# print(res1)

# res3 = 'Вывод:' + (res2 + res1) * res[2]

# print(res3)

# res3 = res2 + res1[2] * res2

# print('Результат:' + res3)

# print(ress)



# Задание 11
# В переменную num из вкладки INPUT попадает число, которое обозначает код символа по таблице ASCII(https://ru.wikipedia.org/wiki/ASCII)
# Определить, является ли введенное число кодом английской буквы.


# num = int(input()) 
# if (num >= 65 and num <= 90) or (num >= 97 and num <= 122): 
#     print(f"Это буква \"{chr(num)}\"") 
# else: 
#     print(f"Это не буква, а символ \"{chr(num)}\"")














# Тип данных словаки (dict) 

# словари - это одна из наиболее часто используемых структук данных, позволяющий хранить обекты
# словарь - изменяемый, итерируемый, неиндуксируемый, упорядоченный тип данных в котором элементы храняться в виде пары ключ значение


# {} - литералы

# dct = {}
# print(type(dct))

# dict_ = {'a': 'hello', 'b':2, 'c':3}

# dict_ = {{'s':5}:5} - None
# print(dict_)

# dict1 = {1:'hello', 2:[1,2,3,4], 4.5:{'a':2}, (1,2,3): 'a'}
# print(dict1[1])

# dct = {'name': 'Jown', 'age': 25, 'hobby': ['fishing', 'footbal', 'dota'] }

# print(dct['hobby'])
# print(dct['hobby'][1])
# data = {'email': 'john@gmail.com', 'password': 'im1m2m333'}

# dict2 = dict([('key1', 'value1'), ('key2', 'value2')])
# print(dict2)

# dict3 = dict(['ab', 'cd','de'])
# print(dict3)


# dict4 = dict()
# dict4['key1'] = 'value1'
# print(dict4)


# dct = dict(age=25)
# print(dct)
# dct['age'] = 23
# print(dct)


# dct = {'age': True, 'age': 78}
# print(dct)


# dict.clear() - очищает словать

# dct = {'name': 'john', 'age': 25}
# dct.clear()
# print(dct)


# import copy

# copy() - возвращает копию словаря

# dct = {'name': 'Ryu', 'age': 18, 'hoppy': ['game', 'anime', 'diving']}
# dct2 = dct.copy()
# dct2['hoppy'][2] = 'hi'
# print(dct2)


# fromkeys[object, value] - создает словать с ключами из object и значием value для всех ключей если не передать value то значение у всех ключей будет None 

# list1 = ['name', 'age', 'hobby']
# dct = dict.fromkeys(list1, 'hi')
# print(dct)

# d = dict.fromkeys('a')
# print(d)

# методы получения элементов словаря

# get(key, default) - возвращает значение по этому ключу

# dct = {'name': 'Ryu', 'age':18}
# print(dct.get('age', 'нет такого ключа'))  # -- выдает None если нет такого ключа
# print(dct['age']) # -- выдает ошибку если такого ключа тен


# update - добавляет новый словарь в наш словарь

# dct = {'name': 'Jack', 'age': 18}
# new_dct = {'hobby': ['game', 'anime']}
# dct.update(new_dct)
# print(dct)


# setdefault - получение значений, работает точно также как get() но если такого ключа нет он создаст новую пару

# dct = {'name': 'Ryu', 'age': 18}
# dct.setdefault('hobby')
# print(dct)


# values() - выводит значение которое есть в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.values()))


# keys() - выводит ключи которые есть в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.keys()))


# items() - выводит все ключи и значение в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.items()))


# pop(key, [message]) - удалет пару ключи и значение и возвращает значениею. если ключа нет то возвращает message (по умаолчанию приходит ошибка)


# dct = {'name': 'Ryu', 'age': 18}
# remove = dct.pop('name')
# print(remove)
# print(dct)


# popitem()  - удаляет и возвращает пару ключ значение удаляет последнюю добавленную пару

# dct = {'name': 'Ryu', 'age': 18}
# # dct['address'] = 'Bischkek'
# remove = dct.popitem()
# print(remove)

# ============================ Задачки =======================

# ==========================1

# dict_ = {'a': 1, 'b': 2, 'c': 3, 'e': 4, 'd': 5, 'y': 6}

# for key,value in dict_.items():

#     if value%2==0:
#         dict_[key] = 0
        

# print(dict_)


# =========================2

# dict_ = {'hello': None, 'python': None, 'javascript': None, 'makers': None}

# for keyl in dict_.keys():
#     dict_[key] = len(keyl)

# print(dict_)


# ========================3

# dict_ = {'John': 60, 'Jack': 70, 'Anton': 85, 'Bake': 81, 'Nastya': 93}

# nums = 0
# for num in dict_.values():
#     nums += num

# number = nums / len(dict_)
# dict_['avarage'] = number
# print(dict_)        



# ====================== tasks 24 avgust

# ====================1

# university = {'программирование': 99, 'экономика': 50, 'медицина': 78}


# university['программирование'] = 23
# univer = {'лингвистика': 87}
# university.update(univer)
# university.pop('медицина')

# print(university)

# sumn = 0
# summ = []
# for i in university.values():
#     sumn += int(i)
    

# print(f'Колв учатнищихся: {sumn}')


# =======================2


# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# dict_swapped = {
# value: key

# for key,value in dict_.items()

# }

# print(dict_swapped)


# ======================3


# gest = int(input('Введите количество гостей которых хотите пригласить: '))

# gests = {}
# number = 0

# while True:
#     number +=1
#     gest1 = input('По одному введите имя гостей которые придут: ')
#     gests[number] = gest1
    
#     if len(gests) == gest: break


# print(gests)



# ========================4



# baylist = {1:'Помидор', 2:'Огурец', 3:'Молоко', 4:'Кефир', 5:'Банан'}

# print(f'Мне нужно купить: {baylist}')

# bayll = len(baylist)

# number = 0
# while len(baylist) != 0:

#     bayed = input("Я купил: ")
#     number += 1
#     if number == 5: break
#     for key,value in baylist.items():
#         if value == bayed:
#             baylist[key] = 0
            
        
        

# print(f'Пора расплататься в кассе Xd')

# for key,value in dict_.items():

#     if value%2==0:
#         dict_[key] = 0
        


# Задание 9
# Создайте словарь a с числовыми значениями. Создайте новый словарь b, такой же как словарь а, но все четные значения замените на 2.

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {} 
# for k, v in a.items(): 
#     if v%2==0: 
#         b.setdefault(k, 2) 
#     else: 
#         b.setdefault(k,v) 
# print(b)




# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# c = {} 
# for k, v in a.items(): 
#     b = v / 5 
#     c.setdefault(k,b) 
# print(c)



# Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным (специальным методом) и распечатайте результат.

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()): 
#     if v % 2 == 0: 
#         del a[k] 
# print(a)



# В переменные a1 , a2 , a3 создайте любые словари тремя возможными способами.

# a1=dict(a=1, b=2, c=3) 
# a2=dict([('d', 4),('e', 5),('f', 6)]) 
# a3=dict([('a', 1)], b=2, c=3) 
# a4=dict({'a' : 1, 'b' : 2}, c=3) 
# print(a1) 
# print(a2) 
# print(a3) 
# print(a4)



# Дан словарь dict1, где ключами будут цены товаров, а значениями их названия, затем пройдитесь циклом по нему и поменяйте все ключи элементов, возведя их в квадрат, новые элементы запишите в словарь dict2

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}

# for k,v in dict1.items(): 
#     dict2.setdefault(k**2,v) 
# print(dict2)




# Из предыдущего словаря dict_, достаньте ключ, значение которого является максимальным, если значений несколько, распечатайте каждый из них по отдельности.

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}

# mm = max(dict_.values())
# for k in dict_.keys():
#     if dict_[k] == mm:
#         print(k)




# Дан словарь dict_, значениями, которого являются словари, измените словарь dict_ таким образом, чтобы значения внутреннего словаря стали внешними значениями

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

# for k,v in list(dict_.items()): 
#     for v2 in v.values(): 
#         dict_[k] = v2 
# print(dict_)


# Дан словарь dict1. Создайте словарь dict2, с ключами как в словаре dict1, а значениями пусть будут произведение чисел внутренних словарей

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}

# for k,v in list(dict1.items()): 
#     res = 1 
#     for j in v.values(): 
#         res = res * j 
#         dict2[k] = res 
# print(dict2)




# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}

# for i in int(list_):
#     if i.isalpha():
#         k = i
#         dict_.setdefault(k,v)
#     elif i%2:
#         v = i
#         dict_.setdefault(k,v)
    
# print(dict_)



# Дан список, состоящий из строк и чисел. Создайте словарь, ключами которого будут строки из списка, а значениями числа

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding'] 

# ls = [x for x in list_ if type(x)==int] 
# ls2 = [x for x in list_ if type(x)==str] 
# dict_ = dict(zip(ls2, ls)) 
# print(dict_)





# Дан словарь dict_. Отсортируйте словарь по значениям в порядке увеличения.
# Новые элементы занесите в словарь sorted_dict

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# sorted_dict = {k:item for item in sorted(dict_.values()) 
# for k,v in dict_.items()
#     if item == v} 
# print(sorted_dict)



# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {k:item 
# for item in sorted(dict_.values(), reverse=True) 
# for k,v in dict_.items() 
# if item == v} 
# print(sorted_dict)




# Дан словарь. Найдите сумму значений словаря, который хранится под ключом vars, используя значение словаря, под ключом math

# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }

# res = dict_.get('vars')

# for k,v in dict_.items():
#     for j in v.values():
#         if type(j) != int:

#             print(j(res.values()))





# a = {'a': 10, 'b': 9, 'c': 3}

# result = 1 

# for k, v in a.items():
    
#     result *= v
    
# print(result)



# нужно создать новый словарь, ключами которого будут буквы строки, а значениями числа, соответствующие количеству повторений данной буквы в строке.

# string = "pythonist" 

# dict_ = {}
# for i in string:
#     lenn = string.count(i)
#     dict_.setdefault(i,lenn)
# print(dict_)













# list - изменяемый, индексируемый, упорядоченный (хранит порядок вставки в него элементов) итерируемый тип данных
# итерируемый обьект - это обьект в котором можно пройтись по каждому элементу (for)

# lisst = []
# list() 

# list_ = [1,2,3, 'hello', [5, 1.2], {'a': 3}]
# print(list_[1])
# print(list_[4][0]) #list_[4] --[0,1.2] --[0]


# names = input('Enter names with spaces: ').lower().split()
# guest = input('Enter your name: ').lower()

# print(names) # ['name', 'name', 'name']


# if guest in names:
#     print('Yes')
# else:
#     print('No')


# my_list = list('hello world')
# print(my_list)


# range() - возвращает последовательносит элементов
# range(0,10) -- создай список числе от 1 до 10, 10 не включается в список

# my_list = list(range(10,2,-1))

# []
# my_list = [1_000_000_000_000]
# print(my_list)

# list3 = [1] * 5
# print(list3)



# Методы списка

# list_ = ['string', 2, 3, 4, 5]
# del list_[0]
# print(list_)
# list_[0] = 1
# print(list_)


# append - добовляет элемент в конец списка и принимает в себя один элемент

# list_ = []
# list_.append(1)
# print(list_)
# list_.append('string')
# list_.append([1,2,3,4,5])
# print(list_)


# extend(element) - расшираяет список добовляя в конец элементы

# list_ = [1,5]
# list_.extend('hello')
# print(list_)

# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)
# print(list1)

# print(list1)


# insert(index,element) - допавляет элемент по указанному индексу

# list1 = [1,2,3]
# last_index = len(list1) + 1
# list1.insert(100,'hello')
# print(list1)


# index(element,start,end) - возвращает индекс элемента

# list_ = [1,2,3,4,5, 6, 7]
# result = list_.index(2,3)
# print(result)


# clear - очищает список

# list_ = [1,2,3,4,5]
# print(list_.clear())


# count - считает количество принятого элемента в списке

# list1 = ['hello',1,2,3,4,5,6,7,8]
# print(list1.count(1))

# len() - считает длину обектов
# list_ = [1,2,[1,3,4],4]
# print(len(list_))


# pop - удаляет элемент по индексу и возвращает его, если индекс не указан, то удаляет последний элемент

# list_ = [1,2,3,4,5]
# popped = list_.pop(1)
# print(list_)
# print(popped)

# remove - удаляет первый принятый элемент в списке

# list_ = [1,2,3,4,5,6]
# removed = list_.remove(1)
# print(list_)
# print(removed)


# reverse = изменяет список расставяя его элементы в обратном порядке

# list_ = [1,2,3,4,5]
# list_.reverse()
# list1 = list_.copy()
# print(list_)


# sort - сортирует список состоящий из элементов одного типа данных в возрастающем порядке(в алфавитном для строк) 
# Если указан reverse=True то список будет отфильтрован в убывающем порядке

# list1 = [1,2,3,4,5,12,22,32,55,54]
# list1.sort(reverse=True)
# print(list1)

# list_ = ['f', 'a', 'b', 's', 'E', 'n']
# list_.sort()
# print(list_)

# list1 = [1,2, 'hello']
# list1.sort()
# print(list1)


# copy = копирует список

# list_ = [1,2,3,4,5,[2,3,4]]
# new_list = list_.copy()
# print(new_list)


# цикл - это блок кода который повторяется несколько раз мы используем цкл в тех случаях, когда нам нужно повторить что нибудь n когличество раз

# for - цикл, который работает с итрируемым объектом
# list str tuple 

# интерируемый обьект - обьект по которому можно проходиться, который способен возвращать элемент по одному

# a = 0 
# for i in a:
#     print(i) 
# Error


# string = 'string'

# for i in string:
#     print(i)

# for элемент in итеруемый обьект

# list1 = [1,2,3,4,5]

# string = 'string'

# for element in string:
#     print(element)


# for i in range(5):
#     print(i)

# for element in 12345:
#     print(element)    - Error



# for i in range(10):
#     if i == 2:
#          print(i)


# for i in range(10):
#     print(i)
#     for j in range(10):
#         print(j)
#         if j == 5:
#             print(5,'j')
    
#     if i == 3:
#         print(2, 'i')

# инкремент - это увеличение значений какой либо переменной
# дикримент - это увеличение значений какой либо переменной

# инкримент

# a = 0
# a = a + 1











# циклы - это блок кода, который повторяется определенное количество раз или работает беспонечно

# for - цикл, который работает  с итерируемыми обьектами и закончит свою работу на последнем элементе

# while - циел, который работает пока условие будет верно

# while True - пока Правда
# после while  идет условие цикла и пока это условие верно, то цикл будет работать

# остановить цикл можно комбинациями ctrl + c или ctrl + z

# while True:
#     print('Hello world')


# counter = 0
# while True:
#     counter += 1
#     print(counter)



# count = 0
# while count != 101:  # --- пока count не равен 101
#     print(count)
#     count += 1
# print('end')



# count = 10
# while count != 0:
#     print(count)
#     count -= 1
#     count = count - 1
# print('end')



# a = 0 
# while a:
#     print('hello') # --- не отработает потому что условие False



# for i in range(1,10):
#     print(i + 1)

# list1 = list(range(1,10))
# print(list1)



# for i in 12345: # --- int' object is not iterable
#     print(i)
# тип данных int не итерируемый обьект



# num = 123345678
# sum = 0 

# for i in str(num):
#     sum += int(i)

# print(sum)



# string = 'hello'
# string1 = 'world'
# for i in range(len(string)):
#     print(i, string[i], string1[i])

# 0 h w
# 1 e o 
# 2 l r  ---- работает только с переменными одинаковой длинны
# 3 l l 
# 4 o d 



# list_ = [1,2,3]  
# for i in list_:    # ---- бесконечный цикл с помощью for
#     print(i)
#     list_.append('hello')
#     print(list_)
#     if len(list_) == 100:
#         break



# ========== ключевые слова в циклах ===========


# break = полностью выйти из цикла досрочно прерывает цикл

# continue = перейти к следующей операции ----------------------usfull




# for i in range(10):
#     if i == 3:
#         continue
#     print(i)



# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
#     print(i)



# for i in range(10):
#     print(i)
#     if i == 3: 
#         break
#     print(i)



# i = 0
# while i < 6:
#     if i == 3: 
#         break
  
#     print(i)
#     i += 1



# for i in range(10):
#     if i < 3: continue
#     print(i)



# for i in range(10):
#     print(i)
#     for j in range(10):
#         print(j)
#         if j == 5:
#             break
#     if i == 2:
#         break



# list_ = [2, 1, 3, 6, 2, 5, 2, 8, 2]

# while 2 in list_:
#     list_.remove(2)
# print(list_)



# while True:
#     print(1)
#     continue
#     print(2)
    


# else примененное в цикле for и while, проверяет, был ли произведен выход из цикла с помощью  break, или же естественным образом
# else работает если выход из цикла был совершен без помощи break 

# for i in 'hello world':
#     if i =='d':
#         break
# else:
#     print('hello world')   # Ничего не выйдет



# for num in range(5):
#     if num < 3:
#         pass           # pass -- функция чтобы не было синтастической ошибки pass = пустота, балванга, пуголо
#     else:
#         print(num)



# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# for key in dict1:
#     print(key)


# for value in dict1:
#     print(dict1[key])



# for items in dict1.items():
#     print(items)



# items = (1,2)
# key,value = items
# print(key,value)


# for items in dict1.items():
#     key = items[0]
#     value = items[1]
#     print(key, value)


# for a,b,c in [(1,2,3), (4,5,6), (7,8,9)]:
#     print(a,b,c)


# operator = input("enter operator + - / *: ")
# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))


# while True:
#     if operator == "+":
#         print(num1 + num2)
  
#     elif operator == "-":
#         print(num1 - num2)

#     elif operator == "*":
#         print(num1 * num2)

#     elif operator == "/":
#         print(num1 / num2)

#     gett = input('Хотите продолжить? Ответ Да или Нет: ')


#     if gett.lower() == 'yes':
#         pass
#     elif gett.lower() == 'no':
#         break
#         print('Вы закончили работу!')
#     else:
#         print('Type Yes or No')
        


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# keys = []
# for key in my_dict:
#     keys.


# =====================Tasks


# while True:
#     password = input("password: ")

#     if len(password) < 8:
#         print("Пароль должен содержать минимум 8 символов")
#         continue
#     elif password.islower() == True:
#         print("Пароль должен содежать хотя бы одну заглавную букву")
#         continue
#     elif password.isupper() == True:
#         print("Пароль должен содержать хотя бы одну строчную букву")
#         continue
#     elif password.isalpha() == True:
#         print("Пароль должен содержать хотя бы одну цифры")
#         continue
#     elif password.isalnum() == True:
#         print("Пароль должен содержать хотя бы специальный символ (например, !, @, #, $ и т.д.")
#         continue
#     else:
#         print(password)
#         break




# name_of_list = ['RyuDzaky']
# nelist = str(name_of_list)
# new_list = list(nelist[2:-2])
# num = int(len(new_list ) / 2)

# if int(len(new_list ))%2 != 0:
#     print(new_list [(num + 1):] + new_list [:(num + 1)])
# else:
#     print(new_list [num:] + new_list [:num])


# string = ['RyuDzakyA']
# strin = string[0]
# center = len(strin) // 2

# piss1 = strin[center:] + strin[0:center]
# piss2 = strin[center+1:] + strin[:center+1]

# if len(strin)%2==0:
#     print(piss1)
# elif len(strin)%2!=0:
#     print(piss2)















# tuple 

# кортеж - неизменяемый тип данных, индексируемый, упорядоченный, итерируемый, предназначенный для зранения любых данных(в целом не отличаются от списков, просто их нельзяизменить и они занимают меньше памяти чем список)


# tuple_ = tuple()
# print(type(tuple_))

# tuple1 = (1,2,3)

# tuple2 = (1,2,3[1,2,3],{'a':1})
# tuple2[3].append(4)
# print(tuple2)


# tuple1 = 1,
# print(type(tuple1))

# tuple3 = tuple('hello')
# print(tuple3)


# ==========Методы tuple===========

# count - считает количество элементов

# tuple1 = (1,2,3,4,5,)
# print(tuple1.count(1))


# tuple1 = ('hello', 'hello', 'hello')
# print(tuple1.count('hello'))

# index - возвращает индекс первого вхождения

# tuple1 = (1,2,3,4,5,1)
# print(tuple1.index(3, 1))

# tuple1 = ([1,2,3], 1, 'h', [4,5,6], '1', 2, [7,8,9])

# tuple1[0].append(2)
# tuple1[3].append(2)
# tuple1[6].append(2)
# for rus in tuple1:
   
#     print(rus)

# for element in tuple1:
#     if type(element) ==list:
#         element.append(2)

# print(tuple1)







# множества и кортежи

# что такое множество 
# синтаксис и основные свойства множеств
# что такое кортеж, основные свойства кортежа
# цикл while

# множества(set)  - изменяемый тип данных, который представяет собой
# неупорядоченную коллекцию уникальных элементов. 
# ОНИ изменяемы, неупорядоченны и уникальны

# МНОЖЕСТВА SET МОЖНО СОЗДАТЬ НЕСКОЛЬКИМИ МЕТОДАМИ. 
# САМЫЙ ПРОСТОЙ ИЗ НИХ ЭТО ЗАДАТЬ МНОЖЕСТВО ПУТЕМ ПЕРЕЧИСЛЕНИЯ
# ЕГО ЭЛЕМЕНТОВ ВНУТРИ ФИГУРНЫХ СКОБОК.

# set1 = {1,2,3}
# print(type(set1))

# ОДНАКО НЕЛЬЗЯ СОЗДАВАТЬ ПУСТОЕ СНОЖЕСТВО, ТАК КАК ОНО СОЗДАСТ
# ПУСТОЙ СЛОВАРЬ

# set1 = {}
# print(type(set1))

# А ЧТОБЫ СОЗДАТЬ ПУСТОЕ МНОЖЕСТВО НЕОБХОДИМО ИСПОЛЬЗОВАТЬ
# ФУНКЦИЮ SET 

# set1 = set()
# print(type(set1))

# свойства множеств
# неупорядоченны. Порядок расположения элементов в множестве
# не имеет значения. А это значит, они не индексируются и не поддерживают 
# операции срезов или же получения индекса по срезу

# изменяемость.
# множества изменяемы и поддердживают 
# обьединение множеств
# добавление элементов
# удаление элементов

# УНИКАЛЬНОСТЬ
# МНОЖЕСТВА ДОЛЖНЫ БЫТЬ УНИКАЛЬНЫМИ А ЭТО ЗНАЧИТ ОНО НЕ МОДЕТ СОДЕРЖАТЬ 
# ОДИНАКОВЫХ ЭЛЕМЕНТОВ

# САМО ПО СЕБЕ МНОЖЕСТВО НЕИЗМЕНЯМЫ И ЕГО МОЖНО МЕНЯТЬ.
# ОДНАКО ЭЛЕМЕНТЫ МНОЖЕСТВА ЯВЛЯЮТСЯ НЕИЗМЕННЫМИ, ОТНОСЯТСЯ
# К НЕИЗМЕНЯЕМЫМ ТИПАМ ДАННЫХ

# ГДЕ ИСПОЛЬЗУЮТСЯ МНОЖЕСТВА
# ЕСЛИ НАМ НУЖНО ПОЛУЧИТЬ УНИКАЛЬНОЕ ЗНАЧЕНИЕ КОТОРОЕ НЕ ПОВТОРЯЕТСЯ

# МЕЖДУ МНОЖЕСТВАМИ МОГУТ БЫТЬ НЕСКОЛЬКО СВЯЗЕЙ ИЛИ ОТНОШЕНИЙ
# 1. РАВНЫЕ МНОЖЕСТВА. 
# ТАК НАЗЫВАЮТСЯ ПОТОМУ ЧТО МОГУТ ИМЕТЬ ДВА МНОЖЕСТВА С 
# ОДИНАКОВЫМИ ЭЛЕМЕНТАМИ
# 2. НЕПЕРСЕКАЮЩИЕСЯ МНОЖЕСТВА
# ТАК ГОВОРЯТ КОГДА МНОЖЕСТВА НЕ ИМЕЮТ ОДИНАКОВЫХ ЭЛЕМЕНТОВ
# 3. ПОДМНОЖЕСТВА И НАДМНОЖЕСТВА

# В ЯЗЫКЕ ПАЙТОН СУЩЕСТВУЮЕТ ТИП ДАННЫХ
# С ХАРАКТЕРИСТИКАМИ МНОЖЕСТВА
# НО С НЕБОЛЬШИМ ОТЛИЧИЕМ А ИМЕННО СВОЙСТВОМ НЕИЗМЕНЯЕМОСТИ
# ТАКОЙ ТИП ДАННЫХ НАЗЫВ. ЗАМОРОЖЕННОЕ МНОЖЕСТВО ИЛИ frozenset
# frozenset - НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ С ХАРАКТЕРИСТИКАМИ МНОЖЕСТВА
# ЗАЧЕМ НАМ НУЖЕН FROZENSET
# ЭТОТ ТИП ДАННЫХ ИСП НЕ ТАК ЧАСТО ВМЕСТО НЕГО ИСПОЛЬЗУЮТ КОРТЕЖ

# TUPLE = УПОРЯДОЧЕННЫЙ ТИП ДАННЫХ КОТОРЫЙ НЕИЗМЕНЯЕТСЯ И ПРЕДСТАВЛЯЕТ 
# ПОСЛЕДОВАТЕЛЬНОСТЬ ЭЛЕМЕНТОВ
  
# ЦИКЛ WHILE  ПОКА 
# ЭТО УНИВЕРСАЛЬНЫЙ ЦИКЛ ЕГО СИНТАКСИС ИДЕТ ТАК

# while True_or_False_expression:
#     do_something

# похож на оператор if

# В while  ПОТОК ВОЗВРАЩАЕТСЯ К ЗАГОЛОВКУ ЦИКЛА И СНОВА ПРОВЕРЯЕТ 
# УСЛОВИЕ. ЕСДИ ЛОГИЧЕСКОЕ ВЫРАЖЕНИЕ ВОЗВРАЩАЕТ True ТО ЦИКЛ
# СНОВА ВЫПОЛНЯЕТСЯ ДО ТЕХ ПОР ПОКА ЛОГИЧЕСКОЕ ВЫРАЖЕНИЕ НЕ ВЫДАСТ False

# с циклом используются опервторы break и continue
# break ДАЕТ ВОЗМОЖНОСТЬ ВЫЙТИ ИЗ ЦИКЛА ПРИ СРАБАТЫВАНИИ 
# ВНЕШНЕГО УСЛОВИЯ
# ПОМЕЩАЕМ ОПРЕТОР BREAK ПОД ОПЕРВТОРОМ WHILE.
# ОБЫЧНО ПОСЛЕ УСЛОВНОГО ОПЕРВТОРА IF
# И ОПЕРАТОР BREAK ПРИВОДИТ К ВЫХОДУ ИЛИ РАЗРЫВУ ИЗ ЦИКЛА

# ОПЕРАТОР CONTINUE
# ДАЕТ ВОЗМОЖНОСТЬ ПРОПУСТИТЬ ЧАСТЬ ЦИКЛА В КОТОРЫЙ СРАБАТЫВАЕТ 
# ВНЕШНИЕ УСЛОВИЯ НО ПОЗВОЛЯЕТ ПРОДОЛЖИТЬ ВЫПОЛНЕНИЯ ЦИКЛА ДО КОНЦА


# empty = set()
# print(type(empty))

# a = {'makers', 4, 9, True, False}
# b = set('makers')
# print(a)
# c = set(range(1,10,2))
# print(c)

# set1 = {'hello', 2, True, [1,2,3]}
# print(set1)

# СПИСОК, СЛОВАРЬИ САМО МНОЖЕСТВО НЕ МОЖЕТ БЫТЬ ВНУТРИ МНОЖЕСТВА ТАК КАК ОНИ ТАКЖЕ ЯВЛЯЮТСЯ
# ИЗМЕНЯЕМЫМИ

# СРАНЕНИЕ МНОЖЕСТВ
# set1 = {1,5,3,9,8}
# set2 = {9,1,5,3,8}
# set3 = {1,5,1,3,3,8,8,8,9,9}
# print(set1 == set2)
# print(set3)
# print(set3 == set2)

# set1 = {1, 1.0, True}   что было вначале то и выводит так как они все равны
# print(set1)

# set3 = {1,5,1,3,3,8,8,8,9,9}   
# print(len(set3))               дает только колво уникальных элементов работает также и со строками




# set1 = {1,2,3,(1,2,3, [1]), 's'}
# print(set1)  # -- unhashable type: 'list'


# Добавление элементов

# add(element)
# apdate(sequence)

# my_set = {1,2,3}
# my_set.add(3)
# my_set.add('hello')
# my_set.add({1,2,3}) # -- unhashable tupe: 'set'
# print(my_set)


# my_set = {1,2}
# my_set.update([1,2,3,4])
# my_set.update({3:'1', 2:"2"})
# my_set.update('string', [1,2,3,4,5])
# print(my_set)


# Удаление элементов

# clear()
# my_set.clear()


# remove() - удаляет элемент, если такого элемента нет, то выдает ошибку

# my_set = {1,2}
# my_set.remove(2)
# my_set.remove(4) # --- KeyError: 4



# discard() - удаляет элемент, если элемента нет то ничего не происходит

# my_set = {1,2}
# my_set.discard(2)
# my_set.discard(4)



# pop() - удаляет случайный элемент из set() и возвращает

# set2 = {1,2,3,2,4,5}
# popped = set2.pop()
# print(popped)



# difference() - 

# set_a.difference(set_b) - выводит элементы которые есть в set_a  но нет в set_b
# set_a - set_b

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1 - set2)  # {1,2}
# print(set1.difference(set2))  # {1,2}



# symmetric_difference() - выводит элементы которые уникальны в обоих множествах
# set_a ^ set_b

# a = {1,2,3,4,5}
# b = {5,6,7,8,9}
# print(a ^ b) # --- {1,2,3,4,6,7,8,9}
# print(a.symmetric_difference(b)) # --- {1,2,3,4,6,7,8,9}



# intersection - выводит похожие элементы из set_a и set_b
# set_a & set_b

# a = {1,2,3,4,5}
# b = {5,6,7,8,9}
# print(a & b) # --- {5}
# print(a.intersection(b)) # --- {5}



# union - соединяет множества
# set_a | set_b

# a = {1,2,3,4,5}
# b = {5,6,7,8,9}
# ab = (a.union(b))
# print(a | b)
# print(a.union(b))
# print(ab)

# my_set = {1,2,3,4}
# my_list = [5,6,7,8] == (5,6,7,8)
# res = my_set.union(my_list)
# print(my_set | my_list) # --- unsupported operand type(s) for |: 'set' and 'list'
# print(res)




# Число 1 соответствует первому множеству в списке a, число 2 второму, а 3 третьему.

# В зависимости от переданного числа, сохраните строку в inp1, в одно из пустых множеств внутри списка a. В остальные множества добавьте строку "default value".

# В конце, выведите получившийся список.

# Например, если пользователь ввел Hello world и 1, то вывод:

# a = [set(), set(), set()] 
# inp1 = input() 
# inp2 = int(input()) 
# i = 0 
# if inp2 == 1: 
#     a[inp2 - 1].update([inp1]) 
#     a[inp2].update(['default value']) 
#     a[inp2 + 1].update(['default value']) 
# elif inp2 == 2: 
#     a[inp2 - 1].update([inp1]) 
#     a[inp2 - 2].update(['default value']) 
#     a[inp2].update(['default value']) 
# elif inp2 == 3: 
#     a[inp2 - 1].update([inp1]) 
#     a[inp2 - 3].update(['default value']) 
#     a[inp2 - 2].update(['default value']) 
# else: 
#     a[0].update(['default value']) 
#     a[1].update(['default value']) 
#     a[2].update(['default value']) 
# print(a)





# comprehension - генерация последовательностей в одну строку используя цикл
# также его называют синтаксическим сахарам


# index = 0

# for i in range(1,10):
#     index += 1

#     index = index + 1



# основной целью использования как list, dict comprehension является упрощение и повышение читаемости кода

# list comprehension - это упрощенный подход к созданию списка который задействует цикл for а также мы можем использовать if else операторы под капотам генератор списков также использует цикл for но по скорости он быстрее потому что не использует метод append()



# list_ = []
# for i in range(1,11):
#     list_.append(i**2)

# print(list_)


# list_ = (i**2 for i in range(1,11))    # результат for элумент in итерируемый обект
# print(list(list_))



# import time

# start_time = time.time()
# list1 = []

# for i in range(100):
#     list1.append(i)

# time1 = time.time() - start_time

# print(time1)


# start_time1 = time.time()  
# list2 = [i for i in range(100)] 
# time2 = time.time() - start_time1
# print(time2)


# list_ = [i for i in range(1,11) if not i%2]
# print(list_)


# list_ = [i for i in range(0,11,2)]
# print(list_)



# list_ = ['hello' for i in range(10)]
# print(list_)



# print([input() for i in range(10)])



# если в условии нужен else, то все условие пишется до for 

# list_ = ['нечетное' if i % 2 else 'четное' for i in range(1,11)]
# print(list_)



# list1 = [1,'hello', 2, 'a', 4.0, '7', 8]

# a = ['нечетное'  if i%2 else 'четное' for i in list1 if type(i) == int or type(i) == float]

# print(a)



# set comrehesion - разница с list comprehesion что выходные данные не содержит дубликатов 


# list_ = [1,2,3,4,5,1,5,5,2]

# set_ = {i for i in list_}

# print(set_)


# list_ = [1,2,3,4,5,1,5,5,2]

# set_ = set()
# for i in list_:
#     set_.add(i)
# print(set_)



# dict comprehesion - аналогично создаются, но обязательно нужно указывать key: value 

# squaeres = {i: i **i for i in range(10)}
# print(squaeres)



# squ = {}

# for k in range(10):
#     squ.setdefault(k,k**k)
#     squ.update({k: k**k})
# print(squ)



# list_ = [1,2,3,4,5,6,7,8]

# dict_ = {i: list_.count(i) for i in list_}

# print(dict_)



# d = {'a': 2, 'c':3}

# dict_ = {k: 'четное' if v %2==0 else 'нечетное' for k,v in d.items()}

# print(dict_)




# dict1 = {k: str(k) for k in range(1,11) }

# print(dict1)



# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']

# dict_ = {list1[index]:list2[index] for index in range(len(list1))}
# print(dict_)




# dict1 = {'a': 1, 'b':2, 'c':3}

# dict2 = {k: v for k,v in dict1.items()}

# print(dict2)



# dict1 = {'a': 1, 'b':2, 'c':3}

# dict2 = {v:k for k,v in dict1.items()}
# print(dict2)



# dict1 = {
#     "a":[1,2,3,4,5],
#     "b":[10,30,2,5],
#     "c":[74,28,47],
#     "d":[4,6,2,92,9]
#     }



# dict2 = {k:sum(v) for k,v in dict1.items()}

# print(dict2)



# list1 = [['hello world' for i in range(5)] for i in range(10)]

# print(list1)



# num = input('Введите число:')
# res = []
# for nums in num:
#     res.append(int(nums))

# print(sum(res))


# new_dict = {k:i for k,v in dict_.items() for i,j in v.items() if j == max(v.values())} 
# print(new_dict)


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:v for k,l in my_dict.items() for c,v in l.items()} 

# print(dict_)



# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# res = [[k[0],k[1]*42] for k in prairie_pirates if k[2]==True]

# print(res)



# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# res = [v['likes'] for v in dict_.values() if v['rating'] > 3 ]

# print(sum(res))



# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# dict1 = [c['id'] for a,b in dict_.items() for c in b['comments'] if len(dict_[a]['comments'])>3]

# print(dict1)


# list_ = [i/2 for i in range(0,11) if i%2==0]

# print(list_)


# set1 = {x for x in range(10)} 
# set2 = {a for a in range(8,18)}

# full_set = set1.union(set2)

# if len(full_set)<20:
#     print(f'В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set)==20:
#     print('Ваш объединенный сет полностью уникальный!')



# word = 'lol'
# word1 = 'lol'

# if word == word1:
#     print('dd')














# list_ = ['abc',1,2,3]

# count = 0

# for i in list_:
#     count+=1
# print(count)



# str_ = 'string'

# count = 0

# for i in str_:
#     count += 1
# print(count)



# def my_len(res):
#     count = 0
#     for i in res:
#         count += 1
#     print(count)           -== Usfull

# str_ = 'string'
# list_ = ['abs',1,2,3]

# my_len(str_)
# my_len(list_)

# функции - это именованный блок кода, который выполняет одну задачу и может принимать в себя оркументы и возвращать какое то значение 
# футкцию можно вызывать много раз, обращаясь по имени


# def - ключевое слово, указывает  python что мы хотим создать функцию
# название функции = это переменная, под этим имененем питон запоминает название этой функции
# скобки - нужный для того, чтобы функция могла принимать параметры


# синтаксис

# def название_функции(агрументы):
    # принимает аргументы для работы в теле название_функции
    # тело функции 

# название_функции(агрументы)


# def my_sum(x,y):
#     print(x+y)
#     return x+y

# my_sum(2,2)
# my_sum('Ryu','Dzaky')
# my_sum(9,0)

# res = my_sum(4,5)
# print(res)



# return - используется для возвращения результата и на этом моменте функция завершает свою работу

# return - это ключевое слово, которое дает понять python что за этой командой будет какя то информация которая является окончательный результатом нашей функции 


# def sum_two_numver(a,v,s):
#     print(a,v,s)

# sum_two_numver(5,3) # TypeError: sum_two_numver() missing 1 required positional argument: 's'


# def sum_two_numver(a,v,s=9):
#      print(a,v,s)

# sum_two_numver(2,3)   # позиционные аргументы
# sum_two_numver(a=2,v=3,s=9)  # - Именованные аргументы



# распаковка list(*), dict(**)

# list1 = list(range(1,11))
# print(list1)
# list1 = [*range(1,11)]  # Распаковываем значение в новый список
# print(list1)


# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {**dict1}
# list3 = [*dict1]
# print(dict2)
# print(list3)



# необязательные оргументы args kwargs 
# args -= принимает позиционные аргументы 
# kwargs -= принимает именнованные аргументы 

# args - tuple 
# kwargs - dict 

# def two_sum(a,b, *args, **kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)
#     return a+b+sum(args) +sum(kwargs.values())

# res = two_sum(2,3,6,9,92,29,39,2,34,5,6,first = 400,second=30)

# print(res)



# def func(a,b=10,*args,**kwargs):
#     print('a',a)
#     print('b',b)
#     print('args -- ',args)
#     print('kwargs -- ', kwargs)

# func(5,3,9,2,'you',kk = 23, vv = 24)

# func(1,c=3,b='df',v=23)



# аннотация - делает код более информативным 


# num: int = 10
# str_: str = 'Hello'


# def func(a,b:str,c:int) ->int :
#     """
#     Заметка как работает функция
#     """
#     print(a+b+c)

# func(1,'str',2)




# list_ = ['olo','lol','hello','world','aziza']

# def palindrom(words:list) -> list:
#     palindrom1 = []
#     for word in words:
#         if word == word[::-1]:
#             palindrom1.append(word)
#         else:
#             continue
#     return palindrom1  # После return ничего не выходит
#     print('Вернии!!!')

# print(palindrom(list_))



# dict1 = {'a': 1, 'b': 2, 'c': None, 'e': 3, 'd': None}

# def funk(key:dict):
#     res = {}
#     for k,v in key.items():
#         if v==None:
#             pass
#         else:
#             res.setdefault(k,v)
#     return res

# print(funk(dict1))



# def valemail(email:str):
#     indx = email.find('@')
#     domains = ['gmail.com','mail.ru']
#     if "@" not in email:
#         raise Exception('Invalid email')
#     elif not email[0:indx]:
#         raise Exception('Invalid email')
#     elif email[indx+1:] not in domains:
#         raise Exception(f'Invalid email domain {domains}')
#     print('Emailis valid and successfully saved')
#     return True

# email = 'rysa@gmail.com'
# # print(valemail(email))



# def ragister(email:str, passwerd1:str, passwerd2:str):
#     db_email = None
#     password = None
#     if valemail(email):
#         db_email = email
#     if passwerd1 != passwerd2:
#         raise Exception('пароли не совпадают')
#     password = passwerd1
#     msg = 'Вы успешно зарегистрировались'
#     return {'email': email, 'password': password, 'msg': msg}

# email = 'rysa@gmail.com'

# passwerd1 = 'rysa9888'
# passwerd2 = 'rysa9888'

# print(ragister(email=email, passwerd1=passwerd1, passwerd2=passwerd2))



# ======================Tasks=================

# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))

# def res(a,b):
#     num = a+b
#     print(num)
#     return num

# res(num1,num2)

# string = input('Enter string: ')

# def res(string:str):
#     str_len = len(string)
#     print(str_len)

# res(string)



# def res(a,b):
#     type1 = type(a)
#     type2 = type(b)
#     print(type1, type2)

# res('RyuDaky', 988)


# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))

# def res(a,b):
#     num = a/b
#     print(num)

# res(num1,num2)



# dict1 = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 

# def res(key:dict):
#     for k,v in key.items():
#         print(k)

# res(dict1)


# num = int(input('Enter num: '))

# def res(n:int):
#     if n%2==0:
#         print("It's odd number")
#     else:
#         print("It's even number")

# res(num)


# string = input("Enter something: ")

# def res(st:str):
#     word = st.replace(' ','')
#     if word.lower() == word[::-1].lower():
#         print('Введённое слово является палиндромом!')
#     else:
#         print('Введённое слово не является палнидромом!')

# res(string)



# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))

# def res(n1:int,n2:int):
#     if n1 > n2:
#         print(f'{n1} больше')
#     elif n1 < n2:
#         print(f'{n2} больше')
#     else:
#         print('Они равны!')

# res(num1,num2)


# num = list(input('Enter numbers: '))

# def res(nums:list):
#     num_sum = 1
    
#     for i in nums:
#         if i.isdigit():
#             num_sum *= int(i)
#     print(num_sum)

# res(num)



# num = input('Enter numbers: ')

# def res(nums:str):

#     num_sum = 0
    
#     for i in nums:
#         if i.isdigit():
#             num_sum += int(i)
#     print(num_sum)

# res(num)



# num = int(input('Enter number: '))
# def nums(num1:int):
#     for i in range(1,num1+1):

#         if num1%2==0 and num1!=2:
#             return('Натуральное число')  
#         elif num1%num1==0 and num1%1==0:
#             return('Простое число')
    
    
# print(nums(num))



# list1 = [1, 4, 6, 2, 1, 3, 6, 8, 2, 6, 7]

# def res(list_:list) -> list:
#     list_ = list(set(list_))
#     list_.sort(reverse=True)
#     return list_


# print(res(list1))




# num1 = int(input('Enber number: '))
# num2 = int(input('Enter number2: '))

# def sum_range(start:int,end:int):
#     summ = 0
#     if start<end:
#         for i in range(start,end+1):
#             summ+=i
#     else:
#         for i in range(end,start+1):
#             summ+=i
#     return summ

# print(sum_range(num1,num2))



# num1 = int(input('Enber number: '))
# num2 = int(input('Enter number2: '))

# def sum_range(start:int,end:int):
#     if start > end:
#         start, end = end, start
#     return sum([i for i in range(start, end + 1)])

# print(sum_range(num1,num2))



# def fuc(list_=[]):
#     res = []
#     res.append(list_)
#     return res

# print(fuc('kjs'))


# def get_sum(num: int) -> int:
     
#     dict_ = []

#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             dict_.append(i)

#     return dict_

# print(get_sum(1098))



# ===================Tusks==============
# import random

# name = input('Введите имя и фамилию: ')

# def get_info(info:str) -> str:

#     part1 = info.replace(' ','')
#     generate_password(part1)
    
# def generate_password(password:str) -> str:

#     part2 = random.randint(1000000,9999999)
#     part3 = password + str(part2)
#     print(part3)


# get_info(name)



        
# operator = input("enter operator + - / *: ")
# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))

# def get_data(num11:int, num22:int , oper:str):
    
#     if operator == "+":
#         res = num1 + num2
#         return res
#     elif operator == "-":
#         res = num1 - num2
#         return res
#     elif operator == "*":
#         res = num1 * num2
#         return res
#     elif operator == "/":
#         res = num1 / num2
#         return res
    
# resss = get_data(num1,num2,operator)


# def result(ress:int):
#     print(ress)

# result(resss)    




# def calc(num1: int, num2: int, oper:str):
#     if oper == '+':
#         add_(num1, num2)
#     elif oper == '-':
#         sub_(num1, num2)
#     elif oper == '/':
#         div_(num1, num2)
#     elif oper == '*':
#         mult_(num1, num2)

# def add_(num1: int, num2: int):
#     res = num1 + num2
#     print(res)

# def sub_(num1: int, num2: int):
#     res = num1 - num2
#     print(res)

# def div_(num1: int, num2: int):
#     res = num1 / num2
#     print(res)

# def mult_(num1: int, num2: int):
#     res = num1 * num2
#     print(res)

# calc(2,3,'+')



# def add_(num1: int, num2: int):
#     return num1 + num2
    
# def sub_(num1: int, num2: int):
#     return num1 - num2
    
# def div_(num1: int, num2: int):
#     return num1 / num2

# def mult_(num1: int, num2: int):
#     return num1 * num2
    
# def result(num1: int, num2: int, oper):
#     if str(oper) == '+':
#         return add_(num1, num2)
#     elif str(oper) == '-':
#         return sub_(num1, num2)
#     elif str(oper) == '/':
#         return div_(num1, num2)
#     elif str(oper) == '*':
#         return mult_(num1, num2)

# result(2,3,'+')





# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]


# def func17(list1:list):
#     list2 = []
#     for i in list1:
#         i['salary'] = i['overTime']*200+i['salary']
#         i.pop('overTime')
#         list2.append(i)

#     return list2

# print(func17(employees))


 


# balance = 2000



# def spent(stuf, spent:int):
#     global balance
#     res = {}
    
#     if spent <= balance:
#         balance -= spent
#         part = {'target': stuf, 'spend': spent}
#         res.update(part)
#     elif spent > balance:
#         print('Ваш кашелек истащен XO')

#     return res



# def deposit(depo:int):
#     global balance
#     balance += depo
#     print(balance)

# print(spent('Anime', 200))
# deposit(800)



# balance = 2000


# def spent(stuf, spent:int, balan:int):
#     global balance
#     res = {}
    
#     if spent <= balan:
#         balance -= spent
#         part = {'target': stuf, 'spend': spent}
#         res.update(part)
#     elif spent > balan:
#         print('Ваш кашелек истащен XO')

#     return res


# def deposit(depo:int):
#     global balance
#     balance += depo
#     return balance
    

    
# res = spent('Anime', 200, balance), deposit(800)
# print(res)




# CRUD

# Create
# Read
# Update
# Delete

# import datetime

# data = [
#     {
#         'id': 1,
#         'name': 'iphon 14',
#         'price': 80000,
#         'created_at': datetime.datetime(2022, 9, 4),
#         'is_active': True
#     },
#     {
#         'id': 2,
#         'name': 'Manga Solo Leveling',
#         'price': 200,
#         'created_at': datetime.datetime(2020, 7, 3),
#         'is_active': True
#     },
#     {
#         'id': 3,
#         'name': 'Anime Blich',
#         'price': 400,
#         'created_at': datetime.datetime(2010, 6, 2),
#         'is_active': False
#     }
# ]


# def get_all():
#     return data

# # print(get_all())



# def get_one(id):
#     for i in data:
#         if i['id'] == id:
#             print(i)

# # get_one(2)




# def post_product():
#     max_id = max([i['id'] for i in data])
#     new_data = {
#         'id': max_id + 1,
#         'name': input('Имя: '),
#         'price': int(input('Цена: ')),
#         'created_at': datetime.datetime.now(),
#         'is_active': True
#     }
#     data.append(new_data)
#     return '201 CREATED', new_data

# # print(post_product())




# def patch_product(id):
#     product = [i for i in data if i['id'] == id]
#     index = data.index(product[0])
#     if product:
#         data.remove(product[0])
#         name = input('Имя: ')
#         price = int(input('Цена: '))
#         product[0]['name'] = name
#         product[0]['price'] = price
#         product[0]['created_at'] = datetime.datetime.now()
#         product[0]['is_active'] = True
#         data.insert(index, product[0])
        
#         return 'Успешно изменено'
#     else:
#         return '404', 'Вы ввели неправильные данные'

# # print(patch_product(3))





# def del_product(id):
#     product = [i for i in data if i['id'] == id]
#     if product:
#         data.remove(product[0])
#         return  'Deleted'
#     else:
#         return 'Has no find'

# # print(del_product(3))




# def main():
#     print('Hello, you have next fanctions:\n\tPOST\n\tGET\n\tDETAIL\n\tPUT\n\tDELETE')
#     method = input('Введите одну из функции: ').upper()

#     if method == 'GET':
#         print(get_all())

#     elif method == 'DETAIL':
#         id = int(input('Введите id: '))
#         print(get_one(id))

#     elif method == 'POST':
#         print(post_product())

#     elif method == 'PUT':
#         id = int(input('Введите id: '))
#         print(patch_product(id))

#     elif method == 'DELETE':
#         id = int(input('Введите id: '))
#         print(del_product(id))

# main()



# ==========================Tasks===========================


# import datetime

# data = [
#     {
#         'id': 1,
#         'category': 'Веб-разработка',
#         'sub_category': 'Python',
#         'header': "WebDev Mastery: Build & Create",
#         'description': "Наш курс по веб-разработке поможет вам освоить современные технологии и навыки для создания впечатляющих веб-сайтов и приложений.",
#         'level': 'начальный',
#         'price': 65000
        

#     },
#     {
#         'id': 2,
#         'category': 'Разработка мобильных приложений',
#         'sub_category': 'JavaScript',
#         'header': "Mobile App Development: Create, Code, Launch",
#         'description': "Научитесь создавать мобильные приложения от идеи до релиза вместе с нашим курсом разработки мобильных приложений.",
#         'level': 'средний',
#         'price': 75000

#     },
#     {
#         'id': 3,
#         'category': 'Разработка игр',
#         'sub_category': 'Java',
#         'header': "Game Development: Create, Code, Play",
#         'description': "Изучите искусство создания захватывающих игр с нашим курсом разработки игр.",
#         'level': 'профессиональный',
#         'price': 90000

#     }
# ]



# def get_all():
#     return data




# def get_one(id):
#     for i in data:
#         if i['id'] == id:
#             print(i)





# def create():
#     max_id = max([i['id'] for i in data])
#     count = 0


#     while count == 0:
#         category = input('Введите категорию (Веб-разработка, Разработка мобильных приложений, Разработка игр): ')
#         if category == 'Веб-разработка' or category == 'Разработка мобильных приложений' or category == 'Разработка игр':
#             count += 1
#             category1 = category

#     while count == 1:
#         sub_category = input('Введите подкатегирий (Python, JavaScript, Java): ')
#         if sub_category == 'Python' or sub_category == 'JavaScript' or sub_category == 'Java':
#             count+=1
#             sub_category1 = sub_category

#     while count == 2:
#         header = input('Введите заголовок курса (максимум 60 символов): ')
#         if len(header.split()) <=60:
#             count += 1
#             header1 = header

#     while count == 3:
#         description = input('Введите описание курса (минимум 10 слов): ')
#         if len(description) >= 10:
#             count += 1
#             description1 = description

#     while count == 4:
#         level = input('Введите уровень курса (начальный, средний, профессиональный): ')
#         if level == 'начальный' or level == 'средний' or level == 'профессиональный':
#             count += 1
#             level1 = level

#     while count == 5:
#         price = int(input('Цена в сомах Например: 80000: '))
#         if type(price) == int:
#             count += 1
#             price1 = price

#     new_data = {
#     'id': max_id + 1,
#     'category': category1,
#     'sub_category': sub_category1,
#     'header': header1,
#     'description': description1,
#     'level': level1,
#     'price': price1

#     }

#     data.append(new_data)
#     return '201 CREATED', new_data





# def update(id):
#     product = [i for i in data if i['id'] == id]
#     index = data.index(product[0])
#     if product:
#         data.remove(product[0])
#         count = 0
#         while count == 0:
#             category = input('Введите категорию (Веб-разработка, Разработка мобильных приложений, Разработка игр): ')
#             if category == 'Веб-разработка' or category == 'Разработка мобильных приложений' or category == 'Разработка игр':
#                 count += 1
#                 category1 = category

#         while count == 1:
#             sub_category = input('Введите подкатегирий (Python, JavaScript, Java): ')
#             if sub_category == 'Python' or sub_category == 'JavaScript' or sub_category == 'Java':
#                 count+=1
#                 sub_category1 = sub_category

#         while count == 2:
#             header = input('Введите заголовок курса (максимум 60 символов): ')
#             if len(header.split()) <=60:
#                 count += 1
#                 header1 = header

#         while count == 3:
#             description = input('Введите описание курса (минимум 10 слов): ')
#             if len(description) >= 10:
#                 count += 1
#                 description1 = description

#         while count == 4:
#             level = input('Введите уровень курса (начальный, средний, профессиональный): ')
#             if level == 'начальный' or level == 'средний' or level == 'профессиональный':
#                 count += 1
#                 level1 = level

#         while count == 5:
#             price = int(input('Цена в сомах Например: 80000: '))
#             if type(price) == int:
#                 count += 1
#                 price1 = price


#         product[0]['category'] = category1
#         product[0]['sub_category'] = sub_category1
#         product[0]['header'] = header1
#         product[0]['description'] = description1
#         product[0]['level'] = level1
#         product[0]['price'] = price1
#         data.insert(index, product[0])
        
#         return 'Успешно изменено'
#     else:
#         return '404', 'Вы ввели неправильные данные'





# def delete(id):
#     product = [i for i in data if i['id'] == id]
#     if product:
#         data.remove(product[0])
#         return  'Deleted'
#     else:
#         return 'Has no find'
    


    
# while True:

#     def main():
#         print('Привет, вам доступны следующие функции:\n\tPOST\n\tGET\n\tDETAIL\n\tPUT\n\tDELETE')
#         method = input('Введите одну из функции: ').upper()

#         if method == 'GET':
#             print(get_all())

#         elif method == 'DETAIL':
#             id = int(input('Введите id: '))
#             print(get_one(id))

#         elif method == 'POST':
#             print(create())


#         elif method == 'PUT':
#             id = int(input('Введите id: '))
#             print(update(id))

#         elif method == 'DELETE':
#             id = int(input('Введите id: '))
#             print(delete(id))


#     main()


    





# database = [
#     {
#      'title': 'str',
#      'price': 33, 
#      'category': 'str'
#      }
# ]

# def create(database,title,price,category):
#     dict1 = {
#         'title': title,
#         'price': price,
#         'category': category
#     }
#     return database.append(dict1)

# create(database, 'anim',233,'anime')

# def read(database):
#     return database

# print(read(database))


# def update(database,index,title,price,category):

    
#     database[index]['title'] = title
#     database[index]['price'] = price
#     database[index]['category'] = category
#     return database


# print(update(database,1,'toto',233,'cara'))


# def delete(database, index):
#     del database[index]
#     return database

# print(delete(database, 1))













# исключения и ошибки - обьекты, которые прерывают работу кода 

# ошибки --= проблема в синтаксисе (которые мы исправляем самостоятельно)

# 1. SyntaxError: забыли элемент где-то , неправильно назвали переменную, забыли литералы у функций и модулей

# 2. IndentationError: ошибка табуляции просто нажимай Tab где нужна 

# 3. TabError: неверная табуляция (смешивание пробелов и табов) 



# исключения --= это код написан верно, но программа работает не так как ожидалось 

# 1. ZeroDivisionError --= выходит при делении на ноль print(23 / 0) /,//,% на 0

# 2. NameError --= исключение выходит, когда мы обращаемся к несуществующей переменной

# 3. IndexError --=  исключение которые выходит, когда обращаемся к несуществующему индексу

# 4. KeyError --=  исключение которое выходит когда мы обращаемся к несуществующему ключу

# 5. ImportError --= исключение которое выходит когда мы импортируем не сущиствующий библиотеку

# 6. ValueError --= когда функцию передаем не тот тип данных

# 7. TypeError --= когда мы пытаемся использовать методы не свойственны какому то типу данных либо же когда мы передаем в функцию больше или меньше аргументов чем она ожидает футкцию

# 8. AttributeError --= выходит когда мы обращяемся к несуществующему аттрибуту или методу обьекта

# 9. BaseException() --= прородитель(все ошибки)




# try except - мы используем это строение чтобы наш код не прекращал работу 

# try:
#     код который может вызвать ошибку
# except:
#     код который сработает если в try вышла ошибка
# else:
#     код который сработает если в try  не вышла ошибка
# finally:
#     код который сработает в любом случае



# try:
#     age = int(input('Введите возраст: '))
# except (ValueError, TypeError):
#     age = int(input('Введите возраст еще раз: '))

# print(age)


# try:
#     a = 2
#     b = 0
#     result = a/b
# except ZeroDivisionError:
#     print('error')



# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')



# try:
#     int('f')
# except ValueError:
#     print('Неверный код')
#     try:
#         3/0
#     except ZeroDivisionError:
#         print('Деление на ноль')




# try:
#     num1  = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     print(num1/num2)
# except (ZeroDivisionError, ValueError):
#     print('Произошла ошибка!')



# try:
#     dict_ = {k: k**2 for k in range(1000) if k%a==0}
# except NameError:
#     print('Переменной а нет')
#     a = int(input('Укажите число: '))
#     dict_ = {k: k**2 for k in range(1000) if k%a==0}
#     print(dict_)
#     try:
#         a = int(input('Укажите число: '))
#         dict_ = {k: k**2 for k in range(1000) if k%a==0}
#         print(dict_)
#     except ValueError:
#         print('а должно быть числом')
#         dict_ = {k: k**2 for k in range(1000) if k%a==0}
#         print(dict_)


# try:
#     num1 = int(input('enter number: '))
#     num2 = int(input('enter number: '))
#     result = num1/num2
#     print(result)
# except ValueError:
#     print('Ты ввел неправильные данные')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')


# dict_ = {'a': 5, 'b': 10, 'c': 15, 'd': 20}

# try:
#     key=input('enter key: ')
#     value = dict_[key]
#     print(value)
# except KeyError:
#     print('Нет такого ключа!')
# else:
#     value *= value
#     print(value,'block else')



# try:
#     result = a*2
#     print(result)
# except Exception as e:
#     print(f'Возникла {e.__class__}')
# finally:
#     a = 5
#     result = a*2
#     print(result, 'block finally')




# raise -= искуственно вызывает ошибку 

# number = int(input('enter: '))

# if number>5:
#     raise 'значение не должно быть больше 5!'




# age = 20

# if age>18:
#     raise Exception('Error')
    



# try:
#     if 2 > 1:
#         raise ValueError
# except ValueError:
#     print('Возраст больше 2')




# element1 = input('Введите чтота: ')
# element2 = input('Введите чтота: ')

# if element1.isdigit() and element2.isdigit():
#     res = int(element1) + int(element2)
#     print(res)
# else:
#     print(element1+element2)



# user = input('Введите пользовательское имя: ')
# username = 'RyuDzaky'
# ID = 3
# dict1 = {ID: username}

# try:
#     for k,v in dict1.items():
#         if v==user:
#             print(f'ID {k}')
#             print(f'Hello my dear freand {v}')
#             print('Спасибо')
#         else:
#             raise ValueError
# except ValueError:
#     print('Введенного юзера нет в базе данных')
#     print('Спасибо!')




# age = int(input('Введите ваш возраст: '))

# try:
#     raise ValueError
# except ValueError:
#     if age <= 0:
#         print('Ваш возраст должен быть больше 0')



# try:
#     def filter_comment(comment:str,banlist:[])-> None: 
        
#         comment1 = comment.replace('.','').replace('!','').replace('?','').replace(',','').lower()
        
#         for i in banlist:

#             if i in comment1:
#                 raise ValueError('Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст')
# except ValueError:
#     pass
    
# filter_comment('Hello, world', ['hello'])
# filter_comment('HelloWorld', ['hello']) 
# filter_comment('ochocientos ochenta y ocho')
# filter_comment('I love this recipe', ['hate', 'unlike', 'liken\'t'])
# filter_comment('Dis? recipe. is i !!UNLike!?!! really much!', ['hate', 'unlike', 'liken\'t']) 











# Пространство имен 


# 1) builtins (встроеннное имен) - все что встроенно в оболочку питона 

# print(dir(__builtins__))


# ==========================================================================


# 2) global - все переменные внутри файла которые мы создали

# globals - возвращает словарь с глобальными переменными 

# a = 8
# b = 'hello'


# print(globals()['a'])
# print(a is globals()['a'])
# globals()['c'] = 'hello'
# globals()['c'] = 'hello world'
# print(globals()['c'])

# x = 10

# def func():
#     global x 
#     x = 20
#     print(x, 'x is local')

# func()
# print(x, 'x is global')

# global - позволяет ментять значение глобальной перменной, находясь в локальной области видимости 


# =====================================================================================


# 3) enclosed - пространство находящиеся между двумя пространствами (между global и local)

# enclosed - она возникает тогда, когда есть вложенность в функции 

# x = 'глобальна область видимости'

# def some_func():
#     x = 'это enclosed  область видимости'
#     print(x)
    
#     def some_func2():
#         x = 'это локальная область видимости'
#         print(x)

#     some_func2()
# print(x)
# some_func()


# def func():
#     a = 'func'   # ---- enclosed пространство
#     def inner_func():
#         a = 'inner_func'   # ----- local пронстранство
#         print(locals)
#     inner_func()
#     print(locals())

# func()
# print(globals())


# ====================================================================================


# 4) local - локальное пронстранство имен 

# по мене выполнения программы python создает разные пронстранства имен и удаляет их 


# def hello():
#     a = 'hello world'
#     print(locals())
#     print(a)

# hello()
# print(locals())



# def func(b, c):
#     a = 4
#     print(locals())

# func(2,3)

# print(locals())


# ===========================
# порядок поуска переменных 

# local -> enclosed -> global -> builtins 



# ====================tast 


# count = 0

# def counter():

#     global count
#     count += 1
#     print(count)

# counter()
# counter()



# def counter1():
#     try:
#         print(count)
#         count += 1
#     except:
#         print('f')

# counter1()
# counter1()




# def outer_function():
#     global a
#     a = 20

#     def inner_function():
#         global a
#         a = 30
#         print('inner function a = ', a)
#     inner_function()
#     print('outer function a = ', a)

# a = 40

# outer_function()



# def func():
#     a = '1'
#     def inner_func():
#         def inner_func2():
#             nonlocal a
#             a = 2
#         inner_func2()
#     inner_func()
#     print(a)

# func()



# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 'edited enclosed x'
#         print(x, 'is local')
#     local()
#     print(x, 'is enclosed')

# enclosed()



# def func():
#     var = 100
#     def nested():
#         nonlocal var
#         var += 100
#     nested()
#     print(var)

# func()



# def count(i):
#     counter = 0

#     def add():
#         nonlocal counter
#         print(counter)
#         counter += 1
    
#     for x in range(i+1):
#         add()

# count(10)



# обычно nonlocal позволяет нам назначать перменные во внешней области, но не в глобальной 



# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 30
#         def inner():
#             nonlocal x
#             x = 'Edited x'
#             print(x, 'inner()')
#         inner()
#     local()
#     print(x, 'enclosed ')

# enclosed()



# ========================================Tusk  ==============

# import random

# words = ['список', 'печатать', 'количество', 'программирование', 'виселица', 'семь смертных грехов']
# geas_try = 3

# def whil():
#     global word
#     word = random.choice(words)


# whil()

# blur_word = '*'*len(word)


# while True:
#     print('Печатается: ', blur_word)
#     print(f'Попыток осталось: {geas_try}')

#     letter = input('Введите одну букту для разгадки слово: ')

#     index = [i for i, c in enumerate(word) if c == letter]
    
#     for i in index:
#         res = list(blur_word)
#         res[i] = letter
#         ress = ''.join(res)
#         blur_word = ress
        
#     if not letter in list(word):
#             geas_try -= 1
#             if geas_try == 0:
#                 print('Вы потратели все попытке ;(', geas_try)
#                 break
#     elif blur_word == word:

#         print('Поздравляю вы угадали расшифровали слово!!!')
#         win = 'победа'
#         break

        
        
# string = 'tonaisuu'
# position = 6
# new_character = 'r'
# temp = list(string)            ============================== USFULL STRING
# temp[position] = new_character
# string = "".join(temp)
# print(string)


# var = 'переменная в foo' 
# def foo(): 
#     global var 
#     var = 'переменная foo' 
#     print('переменная в foo: ', var) 
#     def bar(): 
#         global var 
#         var = 'переменная bar' 
#     bar() 
# foo() 
# print('переменная в foo: ', var)4




# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}


# def post(let:dict):

#     for l,nl in let.items():
#         if nl >= 17:
#             print(f'{l}, Вы можете войти в клуб')
#         else:
#             print(f'{l}, извините, Вы не проходите по age-control')

# post(a)



# a = ['pipi', 'papa', 'mama']
 
# b = [i.title() for i in a]

# print(b)




# def count_symbols(strin:str):
#     glas = 'аоуыэяёюие'
#     soglas = 'нмлрйбвгджзпфктшсхцчщ'
#     left = 'ъь '
#     count_g = 0
#     count_s = 0
#     count_l = 0
#     for i in strin:
#         if i.lower() in glas:
#             count_g += 1
#         elif i.lower() in soglas:
#             count_s += 1
#         elif i.lower() in left:
#             count_l += 1

#     return (f'Количество гласных: {count_g}, согласных: {count_s}, остальных символов: {count_l}')


# print(count_symbols('Ырыскелди'))


# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# def lower_7():
#     global a
#     ar = []
#     for i in a:
#         if i < 7:
#             ar.append(i)
#     return ar
    
    
# print(lower_7())





# pip freeze/ pip3 freeze -- просмотр всех библиотек 

# python3 -m venv venv - создание виртуального окружения

# . venv/bin/activate -- активируем виртуальное окружение 

# deactivate - отключает виртуальное окружение 

# pip3 install - установка библиотеки 



# import requests


# response = requests.get('https://www.youtube.com/')


# print(response.text)













# lambda - анонимная функция(та же самаая функция но без названия)

# lambda параметр : что функция возвращает 

# def add_nums(a,b):
#     return a + b

# print(add_nums(2,3))



# result = lambda a,b : a + b

# print(result(2,3))



# x = lambda a,b,c: (a*b)%c

# print(x(1,6,3))


# dict1 = {1: 5, 3: 5, 6: 2}
# get_keys = lambda x : x.keys()
# print(get_keys(dict1))



# square = lambda a: a ** 2
# print(square(5))


# list1 = [1,2,5,6]
# get_last = lambda ls: ls[-1]
# print(get_last(list1))



# ==================================

# map(function, iterable) - функция которая принимает функцию и итерируемый обьект
# она применяет функцию к каждому элементу в iterables



# map_get = map(int,['1','2','3','4'])
# print(list(map_get))



# nums = [1,2,3,4,5,6]

# def square(num):
#     return num * num

# map_func = map(square, nums)

# print(list(map_func))




# list1 = [1, -8, 22, 98, -88]

# list2 = list(map(lambda x: x>0, list1))

# print(list2)



# func = lambda e: e+1
# res = []
# for e in [1,2,3,4,5,6]:
#     res.append(func(e))

# print(res)



# filter(function, iterable)  - функция принимает первым аргументом другую функцию и итерируемый обьект 
# результато будет последовательность котрые прошли условия filter



# nums = [1,2,3,4,5,6,7,8,9,10]

# res = list(filter(lambda e: e%2==0, nums))

# print(res)



# list1 = ['Ryu', 'Kevin', 'Marko', 'Stiv', 'Raya', 'Ryukaku']

# res = list(filter(lambda i: i[0]=='R', list1))

# print(res)




# list1 = ['Ryu', 'Kevin', 'Marko', 'Stiv', 'Raya', 'Ryukaku']

# def sort1(name):
#     values = 'KRHTHALS'
#     # print(tuple(values))
#     return name.upper().startswith(tuple(values))

# print(sort1('Ryu'))

# res = []

# for name in list1:
#     if sort1(name):
#         res.append(name)

# print(res)


# res2 = list(filter(sort1, list1))
# print(res)




# reduce  -  эта функция принимает функцию и возвращает 1 результат
# (ее убрали из стандартной библиотеки питона так как ей нашли замену sum max)


# from functools import reduce


# lst = [1,2,3,4,5]


# result = reduce(lambda x,y: x+y, lst)
# print(result)



# lst = [1,2,3,4,5,6,7,8]

# def mul(a,b):
#     return a*b

# res = reduce(mul, lst)
# print(res)



# enumerate(iterable, ['start - c какого начинать элемента по дефолту 0'])  -   функция принимает последовательность возвращает tuple состаящий из числа и элемента 


# lst = ['a','bb', 'ccc', 'dddd']

# for i in enumerate(lst[1]):
#     print(i)


# for i in enumerate(lst[1:]):##                 ===================================================== SUPER USFULL 11111111111111
#     print(i) 


# for i in enumerate(lst, 10):
#     print(i)




# lst = ['Ryu','Kage','Fuorandy']

# res = list(enumerate(lst,1))
# print(res)





# zip(iterable, iterable .....) - сопоставляет каждый элемент из intrable со следующим 


# list1 = [1,2,3,4,5,6]
# list2 = ['a','b','c','f','d', 'v']
# list3 = [6,9,0,7,9,8]

# print(list(zip(list1, list2, list3)))
# print(dict(zip(list1,list2)))




# any(iterable) - возвращает True если хотя бы один элемент в iterible имеет значение True


# lst = [1,2,3,4,5]
# lst1 = [0, False]
# res = any(lst)
# res1 = any(lst1)
# print(res)
# print(res1)



# all(iterable) возвращает True если все элементы является True 

# lst = [True,False,True,True]
# print(all(lst))



# '''изменить тип данных значений'''
# dict_ = {1: 2, 3: 4, 5: 6}


# res = list(map(lambda k : str(k), dict_ ))

# print(res)


# """задача при помощи map() заменить значение чисел словами четное.нечетное"""
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = list(map(lambda v:  'четное'  if v%2==0 else 'нечетное', lst))

# print(res)





# =========================Tusks 


# lst = [25,'sdf', 2,33, 1, True]
# part = list(filter(lambda c: type(c) == int, lst))
# res = list(map(lambda v: v**0.5, part))

# print(res)



# from functools import reduce

# lst = ['R','y','u','D','a','k','y']

# # res = reduce(lambda v,s: v+s, lst )

# # print(res)



# lst.remove()

# print(lst)





# =============================Tasks planform






# def decor_func(func):
#     print('Decor func')
#     return func()



# def func2():
#     print('func2')
#     return 'hello'

# def func3():
#     print('func3')
#     return 'world'

# res = decor_func(func2)
# print(res)
# res1 = decor_func(func3)
# print(res1)



# ДЕКОРАТОРЫ  - это функция котораый в свою очередь принимает другую функцию
# ДЕКОРАТОРЫ является функцией высшего порядка - это функции которые могут принять как аргумент любую функцию и вернуть ее 
# Декоратор  модифицирует и улучшает принятую функцию и выдает измененую 



# def func2(func):
#     print('Я буду работать до функции func1')
#     print(func())


# def func1():
#     return 'функция func2 завершилась'

# func2(func1)


# def upper_func(func):
#     def wrapper():
#         original_res = func().upper()
#         # modified_res = original_res.upper()
#         # return modified_res
#         return original_res
#     return wrapper

# @upper_func
# def some_text():
#     return 'Hello World'


# @upper_func
# def some_text1():
#     return 'Hello Union'


# res = upper_func(some_text)
# print(res())

# print(some_text1())

# print(some_text())




# def get_name(name):
#     return name

# def get_age(age):
#     return age

# def get_last_name(last_name):
#     return last_name


# print(get_name('RyuDzaky'))
# print(get_age(23))
# print(get_last_name('Junior'))


# def decorator_func(func):
#     def wrapper(some_info):
#         return 'Вы передали: ' + str(func(some_info))
#     return wrapper


# @decorator_func
# def get_name(name):
#     return name

# @decorator_func
# def get_age(age):
#     return age

# @decorator_func
# def get_last_name(last_name):
#     return last_name


# print(get_name('RyuDzaky'))
# print(get_age(23))
# print(get_last_name('Junior'))




# def func_def(function_to_decorate):  # сюда попадает функция которую нужно задекорировать
#     def wrapper():        # оберточная оболочка для функции
#         print('Я код, который отрабатывает до вызова функции!!!')
#         function_to_decorate()
#         print('А я кот который сработает после!!!')
#     return wrapper     # возвращаем обертку


# @func_def
# def func1():    # функция которую мы задекорируем
#     print('Я функцию func1')


# res = func_def(func1)
# print(res())

# func1()




# если мы используем аргументы у функции, то мы обзательно должны передавать их в декоратор 

# def decorator(func):

#     def wrapper(arg):
#         print(f'Смотри что я принимаю {arg}')
#         func(arg)
#     return wrapper

# @decorator
# def func1(word):
#     print(f'Я принимаю в себя слово {word}')

# func1('RyuDzaky')





# def decorator(func):   # лучше использовать такую запись, она является универсальной для всех функций
#     def wrapper(*args,**kwargs):
#         print(f'Здесь args {args}')
#         print(f'Здесь kwargs {kwargs}')
#         func(*args,**kwargs)
#     return wrapper

# @decorator
# def func_without_parametrs():
#     print('Здесь функция без параметров\n')

# @decorator
# def func_with_parametrs(first_name, last_name):
#     print('Здесь функция с параметрами')
#     print(f'Hello {first_name} {last_name}\n')

# @decorator
# def func_with_parametrs_kwargs(first_name, last_name):
#     print('Здесь функция с параметрами')
#     print(f'Hello {first_name} {last_name}')


# func_without_parametrs()
# func_with_parametrs('Ryu', 'Dzary')
# func_with_parametrs_kwargs(frist_name='Ryu', last_name='Dzary')




# def div(func):
#     print('f1')
#     def wrapper(*args,**kwargs):
#         print(func.__name__)
#         return '<div>' + func(*args, **kwargs) + "</div>"
#     return wrapper

# @div
# def get(name, last_name):
#     print('f2')
#     return name + last_name

# print(get('Ryu', 'Dzaky'))




# def bread(func):
#     def wrapper(*args, **kwargs):
#         return 'bread' + str(func(*args, **kwargs)) + 'bread'
    
#     return wrapper


# def ingridients(func):
#     def wrapper(*args, **kwargs):
#         return 'tomato' + str(func(*args, **kwargs)) + 'salad'
    
#     return wrapper

# @bread
# @ingridients
# def get_sandwich(x):
#     print(x)
#     return x

# print(get_sandwich('sasuges'))

# res = ingridients(get_sandwich('sasuges'))
# res1 = bread(res)



# def decorator_maker(f):
#     print(f)
#     print('Я создаю декораторы')
#     def my_decorator(func):
#         print('Я декоратор, я буду вызван в момент декорации функции')
#         def wrapper():
#             print('Я функция обертка, вызываюсь каздый раз при декорирований функции')
#             return func()
#         print('Я возвращаю обернутую функцию')
#         return wrapper
#     return my_decorator


# @decorator_maker(2)

# def decorate_function():
#     print('Я депорированная функция')

# decorate_function()





# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Функция отработала : {end - start}')
#     return wrapper


# @benchmark
# def call_webpage():
#     import requests
#     webpage = requests.get('https://google.com')


# @benchmark
# def iterate_list():
#     for i in range(50000):
#         print(i)

# call_webpage()
# iterate_list()



# def repeat(num):
#     def goll(gol):
#         def wrapper(func):
#             for i in range(0, num):
#                 print(func)
#         return wrapper
#     return goll

# @repeat(num = 4)
# def function(name):
    
#     print(f'{name}')

# function('RyuDzaky')




# def countdown(seconds):
#     res = []
    
#     def goll(gol):
#         def wrapper(func):
#             for i in range(1, seconds+1):
#                 res.append(i)
#                 if i == seconds:
#                     res.reverse()
#             for k in res:

#                 print(k)
#             if i == seconds:
#                 gol()

#         return wrapper
#     return goll

# @countdown(seconds=5)

# def func():
#     print('Hello world')

# func('s')






# GIT - система контроля версий

# GITHUB - онлийн сервис который предоставляет услуги для храниния ваших проектов(репозиторий)




# git init - инициализация проекта 


# git remote add origin url - добавляет удаленный репозиторий который находится на каком нибуть сервере 


# git pull origin master = (название ветки) - стягиваем изменения с ветки


# git status - показывает статус 


# git add - добавляет файлы в рабочей папке в индекс
# индекс в git - это специальная промежутачная область в которой храняться изменения файлов от рабочей директории до удаленного репозитория


# git add file_name file_name1 - добавляет какой то файл


# git add . - добавляет все файлы 


# git commit - добавляет все файлы которые находяться в индексе(которые добавили с помощью команды git add) она сохраняет локально ваш проект 


# git commit -m 'название комментария' - коментарий для вашего созранения 


# git branch - показывает список веток 


# git branch name_branch - (git branch Ryu) создает новую ветку 


# git checkout name_branch - переключение веток 


# git push name_branch - за отправку кода в удаленный репозиторий 

# git push origin name_Ryu 


# git reset file_name - удаляет файл из индекса 


# git rm (-r если папка) --cached name перестает следить за ним 


# git branch -D name - удаление ветки 


# git merge name_branch - слияние веток 


# git log - список коммитов 


# git push --force origin


# git reset [commit/tag]  - отменить все коммиты после указанного коммита (изменения будут сохранены локально)


# git reset --hard [commit] - принудительно вернуться к указанному коммит

