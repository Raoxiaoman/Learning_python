#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

#map
l = ['raohui','leihUi','jiayou']
print(list(map(str.capitalize,l)))
stri = ['123','343','456']
print(list(map(int,stri)))

#reduce

def prod(l):
    return reduce(lambda x,y:x*y,l)
    
lr = [1,2,3,4,5]
print(prod(lr))

#filter
def is_palindrome(n):
    s = str(n)
    for i in range(0,len(s) // 2):
        if(s[i] != s[len(s)-1-i]):
            return False

    return True

print(list(filter(is_palindrome,range(1,1000))))

def _odd_iter():
    n = 1
    while True:
        n = n + 2 
        yield n

def _not_divisible(n):
    return lambda x:x%n > 0

def _prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible,it)

for n in _prime():
    if n < 1000:
        print(n)
    else:
        break

#sorted
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]
    
l = [('raohui',100),('haha',1),('wuyu',19)]
print(sorted(sorted(l,key=by_name),key=by_score,reverse=True))
