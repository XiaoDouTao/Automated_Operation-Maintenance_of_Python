#!/usr/bin env python
#coding:utf-8

'''
================================================================



 Describe: iterator of python

 Author: XiaoDou

 Update time: Apr/22/2017

 Development environment: CentOS 6.5/python 2.7.12



================================================================
'''


#---------------------------------------------------------------
#
#	 iterator test
#
#---------------------------------------------------------------

lst = range(5)
it = iter(lst)

try:
	while True:
		val = it.next()
		print val
except StopIteration:
	pass
print "------------------------------------------------------\n"


#---------------------------------------------------------------
#
#	define iterator	
#
#---------------------------------------------------------------

class Fabs(object):
	def __init__(self,max):
		self.max = max
		self.n,self.a,self.b = 0,0,1
	def __iter__(self):
		return self
	def next(self):
		if self.n < self.max:
			r = self.b
			self.a,self.b = self.b,self.a+self.b
			self.n = self.n+1
			return r
		raise StopIteration
print Fabs(5)
for key in Fabs(5):
	print key
print "------------------------------------------------------\n"

#---------------------------------------------------------------
#
#	define generator	
#
#---------------------------------------------------------------

g = (x*x for x in range(10))
for n in g:
	print n

