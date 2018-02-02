#!/usr/bin/env python
# -*- coding: utf-8 -*-
def move(n,a,b,c):
    """docstring for move"""
    if n == 1:
        print("move:",a,"->",c);
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
        
move(3,'A','B','C')
    
