#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(my_arr):
    print('Исходный массив: ', my_arr)
    maxi = 0
    n = 1

    while n < len(my_arr):
        for i in range(len(my_arr) - n):
            if my_arr[i] > my_arr[i + 1]:
                maxi = my_arr[i]
                my_arr[i] = my_arr[i + 1]
                my_arr[i + 1] = maxi
        n += 1

    return my_arr


print('Отсортированный массив: ', bubble_sort([1, 5, 7, 4, 2, 8, 3]))
