#!/usr/bin/env python
# coding: utf-8

# ### A Module in Python

# <p>A <b>module</b> is a Python file containing a set of predefined and operational <b>functions</b>, <b>classes</b> and <b>variables</b></p>

# In[2]:


# Below is an example of a geometry module
'''
Module geometry.py
'''

# variables
pi = 3.14159265359
phi = 1.6180

# function that calculates the area
def area(obj):
    if type(obj) == square:
        return obj.a**2
    
# definitions of some classes
class square(object):
    def __init__(self,a):
        self.a = a
        
class triangle(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


# <p>The module above can be imported in another file</p>
