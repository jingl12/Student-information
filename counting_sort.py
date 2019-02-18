# -*- coding: utf-8 -*-
# @Author: jing
# @Date:   2019-02-18 17:00:23
#伪计数排序
#Weak counting sort
'''
思路：
    读取列表元素，作为另一个列表的索引号并标记该位置，遍历该列表，将有标记的索引号依次赋值给新列表作为其元素并返回。
缺点：
    列表元素不能重复，也不能为负数和小数。最最重要的是，列表中的最大值不能太大。
thinking:
    Read the list element as the index number of another list and mark the location, traverse the list, assign the tagged index number to the new list in turn and return it.
Disadvantages:
List elements cannot be repeated, nor can they be negative or decimal.Most importantly, the maximum in the list should not be too large.

'''

l = []

lon = int(input('Please enter the list length:'))

highest = 0

for i in range(lon):
    n = int(input('Please enter list elements n' + str(i+1) +':'))
    if n > highest:
        highest = n
    l += [n]

def counting_sort(l,h):

    seat_list = [0 for i in range(h+1)]

    L = []

    for i in l:
        seat_list[i] = 1

    for i in range(len(seat_list)):
        if seat_list[i] > 0:
            L += [i]

    return L

print(l)
print(counting_sort(l,highest))

