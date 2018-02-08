#!/usr/bin/env python
# -*- coding: utf-8 -*-

class person(object):

    """class for person"""
    __slot__ = ("name","age")
    def __init__(self,name,age):
        """TODO: to be defined1.

        :name: TODO
        :age: TODO

        """
        self._name = name
        self._age = age
        
class student(person):

    """class for student"""

    def __init__(self,name,age,score):
        """TODO: to be defined1. """
        # super(student,self).__init__(name,age)
        person.__init__(self,name, age)
        self._score = score 

    def print(self):
        """print student
        :returns: none

        """
        print("%s:%d" % (self._name,self._score))
        
    def get_grade(self):
        """get grade
        :returns: int

        """
        if(self._score > 90):
            return 'A'
        elif(self._score > 80):
            return 'B'
        elif(self._score > 70):
            return 'C'
        else:
            return 'D'
        
    @property
    def score(self):
        """get Score
        :returns: TODO

        """
        return self._score

    @score.setter
    def score(self,score):
        """set Score
        :returns: TODO

        """
        if score <= 100 and score > 0:
            self._score = score
        else:
            print("error")
        
stu = student("raohui",20,100) 
stu.print();

print(stu.score)
stu.score = 101
print(stu.__dict__)
# print(dir(stu))
if hasattr(stu,'_age'):
    setattr(stu,'_age',25)

print(stu.__dict__)



