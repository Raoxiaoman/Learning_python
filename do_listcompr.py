#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i for i in L1 if isinstance(i,str)]
print(L2)

ls = [x for x in os.listdir()]
print(ls)

hhh = [x+y for x in 'abc' for y in 'kao']
print(hhh)



