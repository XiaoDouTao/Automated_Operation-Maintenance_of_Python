#!/usr/bin env python
#coding:utf-8

'''
================================================================



 Describe: function of python

 Author: XiaoDou

 Update time: Apr/8/2017

 Development environment: CentOS 6.5/python 2.7.12



================================================================
'''

'''
============================================================================
 
	 A simple function test

============================================================================
'''

#------------------define greet_user(username) function--------------------

def greet_user(username):
	print '\n Hello,'+username.title()+'!'

#------------------use greet_user(username) function-----------------------

greet_user('XiaoDou')

print '-------------------------------------------------------------------'



'''
============================================================================

	 two partments function

============================================================================
'''

#------------define describe_pet(animal_type,pet_name) function--------------

def describe_pet(animal_type,pet_name = 'Tom'):
	print "\n I have a "+animal_type+'.'
	print " My "+animal_type+"'s name is "+ pet_name +'.'

	print '-------------------------------------------------------------'

#-------------use describe_pet(animal_type,pet_name) function----------------

describe_pet('cat')

describe_pet('cat','Ludaofu')



'''
============================================================================

	 return value

============================================================================
'''

#-----define name(first_name,last_name) function with return value----------

def name(first_name,last_name):
	full_name = first_name+'.'+last_name
	return full_name.title()
	
#----------use name(first_name,last_name) function--------------------------

User_Name = name('Xiao','Dou')
print '\n '+User_Name

print '-------------------------------------------------------------------'



'''
===========================================================================

 	return dict

===========================================================================
'''

#-----define user_name(first_name,last_name) function with return value------

def user_name(first_name,last_name):
	person = {'first':first_name,'last':last_name}
	return person
	
#----------use user_name(first_name,last_name) function----------------------

User_Name = user_name('Dou','Xiao')
print '\n'
print User_Name

print "---------------------------------------------------------------------"



'''
=============================================================================

	while & function

=============================================================================
'''

#-------------------define function------------------------------------------

print "\nThe login user fast name is:Xiao,and the last name is:Dou"

def login(first_name,last_name):
	full_name = first_name + ' ' +last_name
	return full_name.title()

while True:
	print "\nplease tell me your name"
	print "Enter 'q' to quit"

	f_name = raw_input("First_name:")
	
	if f_name == 'q':
		break
	
	l_name = raw_input("Last_name:")
	
	
	if f_name == 'Xiao' and l_name == 'Dou':
		print "\n Welcome to login this system!" 
		break

print "---------------------------------------------------------------------"



'''
============================================================================

	function & list

============================================================================
'''

#-----------define welcome(users) funciton----------------------------------

print "\nThis is a function test about list"

def welcome(users):
	for name in users:
		message = "Welcome,"+name.title()+"!"
		print message

#---begin to use this function

Users_List = ["XD","XiaoDou","XY","XiaoYa"]

welcome(Users_List)

print "---------------------------------------------------------------------"



'''
============================================================================

	function & modify list

============================================================================
'''

#----------------define modify_list(unprinted_list) function----------------

def modify_list(unprinted_list):
	completeds = []
	
	while unprinted_list:
		current = unprinted_list.pop()
		
		print "printing model:"+current
		completeds.append(current)
		
		print "\nThe following models have been printed:"
		for completed in completeds:
			print completed
		print "\n"

#--------------------use the function---------------------------------------

Unprinted_List = ["ipone","ipad","nokia","oppo"]

modify_list(Unprinted_List)

print "-------------------------------------------------------------------"



'''
============================================================================

	other

============================================================================
'''

#--------------define function----------------------------------------------

def Album():
	while True:
		print "\nEnter 'q' to quit"
		input_singer = raw_input("Please tell me singer: ")
		
		if input_singer == 'q':
			break
		
		input_name = raw_input("Please tell me song of name: ")

		Album_dict = {'Singer':input_singer,'Song_Name':input_name}
		
		print Album_dict

	print "-------------------------------------------------------------"

#---------------use function------------------------------------------------

Album()
