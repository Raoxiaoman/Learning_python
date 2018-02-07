#!/usr/bin/env python
# -*- coding: utf-8 -*-

class person(object):

    """class for person"""

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
        
    def getScore(self):
        """get Score
        :returns: TODO

        """
        return _score
    def setScore(self,score):
        """set Score
        :returns: TODO

        """
        if score <= 100 and score > 0:
            self._score = score
        
stu = student("raohui",20,100) 
stu.print();

print(stu.get_grade())
print(stu.__dict__)
# print(dir(stu))
if hasattr(stu,'_age'):
    setattr(stu,'_age',25)

print(stu.__dict__)



