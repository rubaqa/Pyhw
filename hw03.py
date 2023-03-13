# --- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# import random
# print('Cоздадиим список, вот такой:')
# list1 = []
# for i in range(0,random.randint(2, 11)):
#     list1.append(random.randint(0, 10))
# print(*list1, sep='  ')
# count=1
# sum=0
# for i in list1:
#     if count%2==0:
#         sum += i
#     count+=1
# print(sum)


# --- Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# import random
# print('Cоздадиим список, вот такой:')
# list1 = []
# for i in range(0, random.randint(3, 9)):
#     list1.append(random.randint(1, 10))
# print(*list1, sep='  ')
# list2 = []
# ai = len(list1)-1

# print('А теперь выведем произведения парных элементов:')
# for i in range(len(list1)//2):
#     list2.append(list1[i]*list1[ai])
#     ai -= 1
# if len(list1) % 2 != 0:
#     list2.append(list1[len(list1)//2]*list1[len(list1)//2])

# print(*list2, sep='  ')

# --- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
int10 = int(input('Введите положительно целое число: '))
int2 = []
while True:
    int2.append(int10 % 2)
    int10 = (int10 - (int10 % 2)) // 2    
    if int10 == 0:
        break
int2.reverse()
print(*int2,sep='')