#!/usr/bin env python
#coding:utf-8

'''
================================================================



 Describe: decorator of python

 Author: XiaoDou

 Update time: Apr/16/2017

 Development environment: CentOS 6.5/python 2.7.12



================================================================
'''


#---------------------------------------------------------------
#
#	Decorator	
#
#---------------------------------------------------------------


def outer(fun):
	def inner():
		print 'hello ,this is decorator'
		return fun()
	return inner

@outer
def for_name():
	print 'I am xiaodou:'

@outer
def int_name():
	print 'I am xiaoya'

for_name()
int_name()

print "----------------------------------------------\n"

##---------------define a new decorator-----------------
#
#def func1(func):
#	def func2():
#		print '%s is running'%func.__name__
#		print '%s is running'%foo.__name__
#		return func()
#	return func2
#
#@func1
#def foo():
#	print '%s is running'%foo.__name__
#
#foo()
#print "---------------------------------------------\n"


from time import sleep
import datetime

def arg_func(today = 'sunny'):
	def func1(func):
		def func2():
			print "------------------------------------"
			print "This is %s is runing:"%func.__name__
			print "today\'s weather:",today
			print "------------------------------------"
			return func()
		return func2
	return func1

#arg_func() return's value func1
#func1()    return's value func2
#func2()    return's value func()

@arg_func('sunshine')
def f1():
	today = datetime.datetime.now()
	print "today is %s "%today

f1()
