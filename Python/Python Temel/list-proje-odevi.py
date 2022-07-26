"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""
from typing import Iterable
from six import string_types

inputList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def flatten(alist):
    if alist == []:
        return []
    elif type(alist) is not list:
        return [alist]
    else:
        return flatten(alist[0]) + flatten(alist[1:])
print(flatten(inputList))

"""
2- Verilen listenin içindeki elemanları tersine döndüren
bir fonksiyon yazın. Eğer listenin içindeki elemanlar da
liste içeriyorsa onların elemanlarını da tersine döndürün. 
Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""
inputList = [[1, 2], [3, 4], [5, 6, 7]]
newList = [i[::-1] for i in inputList[::-1]]
print(newList)
