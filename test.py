#!/usr/bin/env python
# -*- coding: utf-8 -*-
s1 = 72
s2 = 85

im = (85-72)/72*100
print("improve:%.3f" %im)

def printclassmate(cm):
    """docstring for printclassmate"""
    for ma in cm:
        print(ma)

classmate=['raohui','hahah','test']
printclassmate(classmate)
print(len(classmate))    

classmate.append('raoa')
printclassmate(classmate)
print(len(classmate))    

classmate.insert(1, "nima")
printclassmate(classmate)
print(len(classmate))    

classmate.pop(2)
printclassmate(classmate)
print(len(classmate))    

classmate[1] = 5
printclassmate(classmate)
print(len(classmate))    


ip = input("input age:")
if ip.isdecimal():
    age = int(ip)
    if age >  18:
        print('You are adults! %d' % age)
    else:
        print('You are children! %d' % age)
else:
    print("error input")


# for i in range(7):
    # print(i)

d = {1:"raohui",2:"qihai"}
for item in d.keys():
    print(item)
    print(d[item])
    

a = [1,3,2]
a.sort()
s = (a)
for item in s:
    print(item)
    

