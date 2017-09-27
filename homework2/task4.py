#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binnarySearch(arr, x):
    i = 0
    j = len(arr) - 1
    found = False
    result = None

    while i <= j and not found:
        mid = (i + j) // 2
        if x == arr[mid]:
            found = True
        else:
            if x < arr[mid]:
                j = mid - 1
            else:
                i = mid + 1

    if found:
        result = 'Индекс искомого элемента: {}'.format(mid)
    else:
        result = 'Элемент не найден!'

    return result


print(binnarySearch([0, 1, 2, 3, 3, 5, 7, ], 2))


