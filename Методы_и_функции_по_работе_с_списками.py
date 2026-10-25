#Добавление и удаление элементов
'''
1. append(item): добавляет элемент item в конец списка
2. insert(index, item): добавляет элемент item в список по индексу index
3. len(list): Встроенная функция, которая возвращает общее количество элементов в списке
4. pop([index]) — Удаляет и возвращает элемент по указанному индексу (по умолчанию удаляет последний элемент).
'''

# Задача #1: Дан список целых чисел. Напишите программу, 
# которая вычисляет сумму всех чётных элементов в этом списке.
'''
a = 0
list_1 = [13, 25, 36, 44, 53, 65]
for i in range(len(list_1)):
    if list_1[i] % 2 == 0:
        a = a + list_1[i]
print(a)
'''

#Здача №2: Дан список чисел. Найдите максимальный и минимальный элементы в списке,
# а также их индексы. Без использования встроенных функций max() и min().
'''
a = 0
b = 100000
list_1 = [13, 25, 36, 44, 53, 65]
for i in range(len(list_1)):
    if list_1[i] > a:
        a = list_1[i]
    if list_1[i] < b:
        b = list_1[i]
print(f'Максимальное число: {a}')
print(f'Минимальное число: {b}')
'''
'''
#Задача №3: Напишите функцию, которая разворачивает список
# (переворачивает его задом наперед) без использования срезов вроде [::-1] или метода .reverse().
list_1 = [13, 25, 36, 44, 53, 65]
list_2 = []
for i in list_1:
    list_2.insert(0, i)
print(list_2)
'''
'''
# Задача №4 -- Удаление дубликатов 
nums = [1, 3, 3, 3, 1, 4]
new_list = []
for i in range(len(nums)):
    if nums[i] not in new_list:
        new_list.append(nums[i])
print(new_list)
'''
'''
# Задача №5 среднее арифметическое:
nums = [1, 2, 2, 3, 1, 4]
n = 0
a = 0
for i in range(len(nums)):
    n = n + 1
    a = a + nums[i]
print(a/n)
'''
'''
# Задача №6 кол-во повторяющихся элементов в списке:
nums = [1, 3, 3, 3, 1, 4]
new_list = []
other_list = []
for i in range(len(nums)):
    if nums[i] not in new_list:
        new_list.append(nums[i])
    elif nums[i] not in other_list:
        other_list.append(nums[i])
print(len(other_list))
print(other_list)
'''