#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def sort_insert(arr):
    print('Исходный массив: ', arr)
    for i in range(len(arr)):
        maxi = 0
        while i > 0 and arr[i] < arr[i - 1]:
            maxi = arr[i - 1]
            arr[i - 1] = arr[i]
            arr[i] = maxi
            i -= 1

    return arr


print('Отсортированный массив: ', sort_insert([3, 3, 1, 7, 2, 5, 0]))
