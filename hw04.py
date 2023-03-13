#1. Вычислить число  Пи c заданной точностью d
# import math
# d = input("С какой точность считаем Пи? ")
# count = 0
# if '.' in d:
#     num = d.split('.')[1]
# for i in num:
#     count+=1
# print("Пи равно ", round((math.pi), count))

#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = int(input("Задайте число N: "))
# i = 2
# list = []
# while i <= N:
#     if N % i == 0:
#         list.append(i)
#         N = N // i
#     i +=1
# print(f'Такие множители у N получились -', list)

#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
n = int(input("Сколько элементов? "))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 10))
print('Cделан такой список -', list1)
list2 = []
for j in list1: 
    if j not in list2:
        list2.append(j)   
print('И получен такой список уникальных элементов -', list2)