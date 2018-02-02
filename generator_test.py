#!/usr/bin/env python
# -*- coding: utf-8 -*-


def triangle(Max):
    """docstring for triangle"""
    l=[1]
    while Max  > 0:
        ll = l.copy()
        yield ll
        Max = Max - 1
        if len(l) == 1:
            ll.append(1)
        else:
            for index,x in enumerate(l):
                if index == len(l) - 1:
                    ll.append(1)
                else:
                    ll[index+1] = l[index] + l[index+1]
        l = ll
    return 'done'

for i in triangle(5):
    print(i)

print(next(triangle(5)))

l = (x for x in range(5))
print(next(l))




