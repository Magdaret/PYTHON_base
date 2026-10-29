'''
number_1= int(input("Введите число: "))
for i in range(number_1):
    total_sum = total_sum + i

print(total_sum) '''

'''
tablnum = int(input("Число для которого состовляем таблицу множение (от 0 до 10): "))
for i in range(11):
    a = tablnum*i
    result = f"{tablnum}X{i}={a}"
    print(result)
'''
'''
for i in range(101):
    if i%2 == 0 and (i != 0):
        print(i)

 '''  
'''
sums = 0
num = int(input())
for i in range(num):
    sums = sums + (num*i)
print(sums)
'''
'''
a = 11
while a != 0:
    a = a - 1 
    print(a)
    if a == 1: 
        print("Поехали!")
        break
'''
'''
#Задача №2 данны два числа а и b вывести прямоугольник шириной а, длинной b
a = int(input("Введите длину: "))
b = int(input("Введите ширину: "))
for i in range(a):
    for j in range(b):
        print("*", end = "")
    print()


#Задача №3 вывести треугольник высотой n
n = 4
a = 0
for i in range(n):
    a = a + 1
    for j in range(a):
        print("*", end = '')
    print()
'''
'''
#Задача №4 — числовая лестница:
n = 4
a = 1
for i in range(n):
    for j in range(1,a+1):
        print(j, end = '')
    a = a + 1
    print()
'''
# Задача №5 -- Таблица умножения
c = 10
for i in range(1,c+1):
    for j in range(1,c+1):
        N = i*j
        print(N, '', end = '')
    print()