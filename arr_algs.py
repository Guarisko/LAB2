import random


def arr_min(arr):
    mini = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < mini:
            mini = arr[i]
    return mini


def avg(arr):
    summ = 0
    for x in arr:
        summ += x
    summ /= len(arr)
    return summ


array = [4, 7, 8, 1, 3, 0, 3, -5, 6];
print(arr_min(array))
print(avg(array))
print(array)