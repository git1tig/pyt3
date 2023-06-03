# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
import math
num = int(input("Какое число исходное?"))
n = int(input("А размер массива какой?"))
pos = 0
myArr = [random.randint(1, 10) for i in range(n)]
print (myArr)
mynum = abs(myArr[0] - num)
for i in range(n):
    print (abs(myArr[i] - num), ' * ')
    if abs(myArr[i] - num) < mynum:
            pos = i
            mynum = abs(myArr[i] - num)
print(f'Число c порядковым номером {pos+1} в массиве {myArr} больше всего похоже на {num}!')

