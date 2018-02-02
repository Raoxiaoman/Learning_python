#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Iterable

L=[]
for item in range(100):
    L.append(item)

print(L[:10])
print(L[-10:])
print(L[::5])

T=(L[::5],)
print(T[::5])

