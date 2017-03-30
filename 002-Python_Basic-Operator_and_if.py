#!/usr/bin/env python

# ================================================================
# Describe: This is about Operator and if statement of python
# Author: XiaoDou
# Update time: Mar/30/2017
# Development environment: CentOS 6.5/python 2.7.12
# ================================================================

#
# Test operator about "**" operator
#

print "This is a test about '**' operator:"

a = 2
b = 3
c = a**b

print "a=2,b=3,c=a**b --> c="
print c 

print "------------------------------------------"
print "\n"

#
# Test operator about "//" operator
#

print "This is a test about '//' operator:"

var1 = 9
var2 = 2
var3 = var1//var2

print "var1=9,var2=2,var3=var1//var2 --> var3="
print var3

print "------------------------------------------"
print "\n"

#
# Test operator about "in" and "not in" operator
#

print "This is a test about 'in' and 'not in' operator:"

in1 = 1
in2 = 'xiaodou'

list = [1,2,3]

# Test about "in" operator

if (in1 in list):
	print "in1 in list"
else:
	print "in1 not in list"

# Test about "not in" operator

if (in2 not in list):
	print "xiaodou not in list"
else:
	print "xiaodou in list"

print "------------------------------------------"
print "\n"

#
# Test operator about "is" and "not is"
#

print "This is a test about 'is' and 'not is' operator:"

isa = 10
isb = 'xiaodou'

if (isa is isb):
	print "isa and isb from common project"
else:
	print "isa and isb from different project"

'''
if (isa is not isb):
	print "isa and isb from different project"
else:
	print "isa and isb from common project"
'''

print "------------------------------------------"
print "\n"


#
# Test about if statement
#

username = 'admin'
password = 'xiaodou'

user_input = raw_input('Please input your username:')
pass_input = raw_input('Please inptu your password:')

if username == user_input and password == pass_input:
	print 'Welcome to login %s'%user_input
elif user_input == 'public':
	print 'Login successful,but you just can  read the file'
else:
	print 'Login faild,%s username or password error'%user_input

print "------------------------------------------"
print "\n"
