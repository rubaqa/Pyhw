# --- Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# x = str(input('Введите вещественное число - '))
# sum = 0
# for i in x:
#     if i.isdigit():
#         sum += int(i)
# print(sum)


# --- Напишите программу, которая принимает на вход число N и выдает набор  произведений чисел от 1 до N.
# N = int(input('Введите число до которого нужно показать факториал - '))
# res = []
# x = 1
# tmp =1
# for i in range(1,N+1):
#     while x <= i:
#         tmp = tmp * x
#         x+=1
#     res.append(tmp)
# print(res)


# --- Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# n = int(input('Введите число до которого нужно показать последовательность - '))
# res = []
# sum =0
# print(f'Для n = {n} последовательность будет такая', end=' ')
# for i in range(1,n+1):
#     print(f'{i} : {round((1 + 1/i)**i, 2)}', end='  ')
#     res.append(round((1 + 1/i)**i, 2))
#     sum+=round((1 + 1/i)**i, 2)
# print()
# print(f'А сумма равна {sum}')


# --- Реализуйте алгоритм перемешивания списка.
import random

print('Cначала создадиим список, вот такой:')
list1 = []
list2 = []
for i in range(0,10):
    list1.append(i)
print(*list1, sep='  ')
print('А теперь перемешаем и получим вот такой:')
while len(list1) > 0:
     tmp = random.randint(0, len(list1)-1)
     list2.append(list1.pop(tmp))
     tmp -= 1
print(*list2, sep='  ')