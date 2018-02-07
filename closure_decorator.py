#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
from types import FunctionType

def log(text):
    if isinstance(text,FunctionType):
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print("%s" % (text.__name__))
            return text(*args,**kw)
        return wrapper 
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print("%s %s" % (text,func.__name__))
                return func(*args,**kw)
            return wrapper 
        return decorator

def count():
    fs = []
    def f(i):
        @log("test the")
        def g():
            return i*i
        return g
    for j in range(1,4):
        fs.append(f(j))
    return fs

(f1,f2,f3)= count()

print(f1)
print(f2)
print(f3)

print(f1())
print(f2())
print(f3())


