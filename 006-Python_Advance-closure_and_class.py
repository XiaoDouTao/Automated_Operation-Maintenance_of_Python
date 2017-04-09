#!/usr/bin env python
#coding:utf-8

'''
================================================================


 Describe: closure and class of python

 Author: XiaoDou

 Update time: Apr/8/2017

 Development environment: CentOS 6.5/python 2.7.12


================================================================
'''

'''
================================================================

	closure

================================================================
'''

#-----------define closure--------------------------------------

def addx(x):
	# Now define a closure:addr(y)
	def addr(y):
		return x+y
	return addr

#-----------use closure-----------------------------------------

print "This is a closure test !\n"

c = addx(8)
print "The closure of name is:  "+c.__name__
print c(10)

print "-----------------------------------------------------------"



'''
#--------This is a classical error about closure-----------------
def foo():
	a = 1	#a = [1]
	def inner():
		a = a+1	#a[0] = a[0]+1 # a not define;list a already defined
		return a  #return a[0]
	return inner

c = foo
print c()

print "-----------------------------------------------------------"

#----------------------------------------------------------------
'''


'''
=================================================================

	self

=================================================================
'''

#-----------define a Ball class----------------------------------
class Ball:
	def setname(self,name):
		self.name = name
	def click(self):
		print "I'm %s,Who call me?"%self.name

print "This is a self test !\n"

a = Ball()
a.setname('A')
a.click()

print "-----------------------------------------------------------"


'''
==================================================================

	Class

==================================================================
'''

#-------------------define a Car class----------------------------
class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.reading = 0
	def get_name(self):
		long_name = str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
	def read_course(self):
		print "The course is "+str(self.reading)
	def update_course(self):
		mileage = raw_input('Please input the update value: ')
		print "Your input value is: %s"%mileage
		if mileage > self.reading:
			self.reading = mileage
		else:
			print "You can't roll back an course"
	def increment(self):
		kilometre = raw_input('Please input the increment value: ')
		print "Your input value is: %s"%kilometre
		if kilometre >= 0:
			self.reading += kilometre
		else:
			print "You can't roll back an course"

#-------------------use the Car class----------------------------
print "This is a class test!\n"

my_newcar = Car('audi','a8','2016')

print(my_newcar.get_name())

print "This old course is: "
my_newcar.read_course()

my_newcar.update_course()
my_newcar.read_course()

print "This is increment course test: "
my_newcar.increment()
my_newcar.read_course()
print "-----------------------------------------------------------"
