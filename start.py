#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Basic Printing
print("we're gonna do it")
print('Hi'+'there')

# Basic function
def simple(num1,num2=5):
	print(num1,num2)

simple(5,6)

# global variable
x = 6

def example():
	globx = x
	print(globx)
	globx+=1
	return globx

x = example()

#python is a object-oriented programming
# we can define a class
class calculator:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def addition(self):
		add = self.x + self.y
		print(add)

	def subtraction(self):
		sub =  self.x - self.y
		print(sub)

cal = calculator(3,5)
cal.addition()

# The below code give examples of manipulating a list with number elements
# if first time use statistics, you need to download the package first using pip install statistics
import statistics as s
##from statistics import variance as v, mean as m
##from statistics import * #import everything

example_list=[1,4,6,7,4,5,6,3,4,6]

x = s.variance(example_list)

print(x)

x = [2,3,4,6,8,9,3,1,6]

print(x.count(6))

x.sort()

print(x)

# a list elment can also be a list
# multi-demensional list
x=[[5,6],[7,6],[8,7],2]

print(x[3])





