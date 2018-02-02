#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc(*number):
    """clas number

    :*number: TODO
    :returns: TODO

    """
    ssum = 0
    for item in number:
        ssum = ssum + item
    return ssum,number

num = [3,4,6]
print(calc(*num))
numt = (7,8,9)
print(calc(*numt))
print(calc(1,2,3))

ssum,number = calc(1,1,1)
print(number)


def persion(name,age,**other):
    """persion information

    :name: TODO
    :age: TODO
    :**other: TODO
    :returns: TODO

    """
    print('name:',name,"age:",age,"other:",other)

persion("raohui",25,sex='man')
persion("leihui",22,**{"sex":"woman"})

