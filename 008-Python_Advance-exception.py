#!/usr/bin env python
#coding:utf-8

'''
================================================================



 Describe: exception of python

 Author: XiaoDou

 Update time: Apr/12/2017

 Development environment: CentOS 6.5/python 2.7.12



================================================================
'''


#---------------------------------------------------------------
#
#	try...except...else
#
#---------------------------------------------------------------

print "Give me a number,and I'll devide them."
print "Enter 'q' to quit."

while True:
	first_number = raw_input('\nfirst number: ')
	if first_number == 'q':
		break
	
	seconde_number = raw_input('\nseconde number: ')
	if seconde_number == 'q':
		break
	
	try: # this is just have error code,maybe
	
		# maybe,the will appear error:ZeroDivisionError 
		answer = int(first_number)/int(seconde_number)
	
	# if appear error with ZeroDivisionError,the will run those code:
	except ZeroDivisionError:
		print "you can't divide by 0!"
		break

	# if try block run successful,the will run those code:
	else:
		print answer
print "-------------------------------------------------------\n"



#---------------------------------------------------------------
#
#	try...except...finally
#
#---------------------------------------------------------------

#FileName = 'text.md'
#
#try:
#	file = open(FileName)
#except FileNotFoundError  # bug
#	print('you need this file,I create it aleady')
#	file = open(FileName,'w')
#finally:
#	file.close()


#---------------------------------------------------------------
#
#	try...except...else & json.dump() json.load()
#
#---------------------------------------------------------------

filename = 'username.json'

import json

try:
	with open(filename) as file:
		username = json.load(file)
except:
	username = raw_input('What is your name: ')
	with open(filename,'w') as file:
		json.dump(username,file)
	print "We'll remember you when you come back "+username
else:
	print "Welcome back "+username

print "-------------------------------------------------------\n"
