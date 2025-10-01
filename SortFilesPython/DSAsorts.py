#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
import random
from random import Random

import numpy as np


def getArrLen(a: np.ndarray[tuple[int], np.dtype[np.signedinteger]] | list) -> int:
    temp = 0
    for _ in a:
        temp += 1
    return temp

def compareArr(a: list | np.ndarray[tuple[int], np.dtype[np.signedinteger]], b: list | np.ndarray[tuple[int], np.dtype[np.signedinteger]]) -> bool:
    if getArrLen(a) != getArrLen(b):
        raise Exception(f"length of {a} and {b} do not match")
    else:
        temp = True
        for i in range(getArrLen(a)):
            if a[i] != b[i]:
                temp = False
        return temp
def bubbleSort(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]]) -> np.ndarray[tuple[int], np.dtype[np.signedinteger]]:
    arrLen = getArrLen(arr)
    for i in range(arrLen-1):
        changed = False
        for j in range(arrLen-i-1):
            if arr[j] > arr[j+1]:
                changed = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not changed:
            return arr
    return arr




def insertionSort(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]]) -> list:
    for i in range(1, len(arr)):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

def selectionSort(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]]) -> list:
    for i in range(getArrLen(arr)-1):
        min = i
        for j in range(i+1, getArrLen(arr)-1):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def mergeSort(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]]) -> list:
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]], leftIdx, rightIdx) -> list:
    ...

def merge(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]], leftIdx, midIdx, rightIdx) -> list:
    ...

def quickSort(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]]) -> list:
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]], leftIdx, rightIdx) -> list:
    ...

def doPartitioning(arr: np.ndarray[tuple[int], np.dtype[np.signedinteger]], leftIdx, rightIdx, pivotIdx) -> list:
    ...


if __name__ == "__main__":
    arr = np.arange(10)
#    for i in range(10):
#        x = random.randint(0, len(arr)-1)
#        y = random.randint(0, len(arr)-1)
#        arr[x], arr[y] = arr[y], arr[x]
    arr = arr[::-1]
    print(arr)
    print(bubbleSort(arr))