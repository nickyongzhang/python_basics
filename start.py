print("we're gonna do it")
print('Hi'+'there')

def simple(num1,num2=5):
	print(num1,num2)

simple(5,6)

x = 6

def example():
	globx = x
	print(globx)
	globx+=1
	return globx

x = example()

class calculator:
	def addition(x,y):
		add=x+y
		print(add)

	def subtraction(x,y):
		sub=x-y
		print(sub)

calculator.addition(3,5)

def epic():
        print('wow this is great')

if __name__=='__main__':
        print('such a great module!')


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

# multi-demensional list
x=[[5,6],[7,6],[8,7],2]

print(x[3])





