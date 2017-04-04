#!/usr/bin/env python

# ================================================================
#
# Describe: for and while statement
# Author: XiaoDou
# Update time: Apr/4/2017
# Development environment: CentOS 6.5/python 2.7.12
#
# ================================================================

#
# range(start,end,inc) function test
#

print "This is a range function test:"

for i in range(0,20,2):
	print i

print "----------------------------------------------------------"
print "\n"

#
# This is break test
#

print "This is a break statement test:"

for i in 'xiaodou':
	if i=='d':
		break
	print ('xiaodou:',i)

print "----------------------------------------------------------"
print "\n"

#
# This is continue test
#

print "This is continue statement test:"

for i in 'xiaodou':
	if i=='d':
		continue
	print ('xiaodou:',i)

print "----------------------------------------------------------"
print "\n"

#
# This is while statement test
#

print "This is while statement test:"

sum = 0
count = 1

while count <= 100:
	sum += count
	count += 1
print 'sum 1~100 is:%s'%sum

print "----------------------------------------------------------"
print "\n"

#
# This is list test
#

print "This is list test :\n"

shop_list = ['iphone7','mac','ipad','iphone5s','meizu','xiaomi','gnee']

print "Show all list number:"
print shop_list

print "\n"

print "How many numbers in the list ?"
print len(shop_list)

print "\n"

print "Show the last numbers:-1"
print shop_list[-1]

print "\n"

print "slice :[:-2]"
print shop_list[:-2]

print "\n"

print "slice:[-2:]"
print shop_list[-2:]

print "\n"

print "slice:[1:5:2]"
print shop_list[1:5:2]

print "\n"

print "slice:[::2]"
print shop_list[::2]

print "----------------------------------------------------------"
print "\n"

#
# Tuple test
#

import random

winlist = [['stone','shears'],['shears','cloth'],['cloth','stone']]
choicelist = ('stone','shears','cloth')

prompt = ''' You can choice list as this:
(0) stone
(1) shears
(2) cloth
(3) quit
Please input your choice(with number)'''

while True:
	choicenum = int(raw_input(prompt))
	if choicenum == 3:
		break
	userchoice = choicelist[choicenum]
	comchoice = random.choice(choicelist)
	bothchoice = [userchoice,comchoice]
	
	print "you choice is %s,and comptur choice is %s"%(userchoice,comchoice)
	
	if userchoice == comchoice:
		print "PS\n"
	elif bothchoice in winlist:
		print "You win!\n"
	else:
		print "You faild !\n"
