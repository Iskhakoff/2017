#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sort_select(arr):
    print('Исходный массив', arr)
    for i in range(len(arr) - 1):
        mini = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[mini]:
                mini = j
            j += 1
        dummy = arr[i]
        arr[i] = arr[mini]
        arr[mini] = dummy

    return arr


print('Отсортированный массив: ', sort_select([5, 20, 3, 11, 1, 17, 3, 12, 8, 10]))
