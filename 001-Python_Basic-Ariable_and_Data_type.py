#!/usr/bin/env python

# ================================================================
# Describe: This is a test about print varual data type
# Author: XiaoDou
# Update time: Mar/29/2017
# Development environment: CentOS 6.5/python 2.7.12
# ================================================================

#
# This is a test of int data type
#

intvar = 1
print "This is int of data type:"
print type(intvar)
print "-----------------------------------"
print "\n"



#
# This is a test of float data type
#

floatvar = 3.14
print "This is float of data type:"
print type(floatvar)
print "-----------------------------------"
print "\n"



#
# This is a test of string data type
#

strvar = "my name is xiaodou"
print "This is string of data type:"
print type(strvar)
print "-----------------------------------"
print "\n"



#
# String test !
#
name = 'I love you'

print "The name string variable is:"
print name
print "-----------------------------------"
print "\n"

# The first word is capitalize
print "The first word is capitalized:"
print name.title()
print "-----------------------------------"
print "\n"

# UpperCase function UpperCase
print "All words are UpperCased:"
print name.upper()
print "-----------------------------------"
print "\n"

# Lowercase function lowercase
print "All words are lowercase:"
print name.lower()
print "-----------------------------------"
print "\n"


#
# Character mosaic test !
#

first_name = 'Xiao'
last_name = 'Dou'
full_name = first_name+' '+last_name

Welcome_Words = 'hello,'+full_name.title()+'!'

print "This is Character mosaic test :"
print Welcome_Words
print "-----------------------------------"
print '\n'

#
# list data type test !
#

list = ['Xiao',123,456,'Dou',3.1415926]
tinylist = ['hello',789]

# Show of all list
print 'This are all list data of list:'
print list
print "-----------------------------------"
print '\n'

print "-----------------------------------"
print 'This are all list data of tinylist:'
print tinylist
print "-----------------------------------"
print "\n"

# Show the first list data
print 'Show the first list data:'
print list[0]
print "-----------------------------------"
print "\n"

# Show the second word to the third word from list data
print 'Show the second word to the third word from list data:'
print list[1:3]
print "-----------------------------------"
print "\n"

# Show the words afer the third word(contain the third word) from list data
print "Show the words afer the third word(contain the third word) from list data:"
print list[2:]
print "-----------------------------------"
print "\n"

# Show the tinylist data two times 
print "Show the list data two times:"
print tinylist*2
print "-----------------------------------"
print "\n"

# Show the link list of tinylist and list
print "link list of tinylist and list:"
print tinylist+list
print "-----------------------------------"
print "\n"

# Modify the list variable in the list 
print "Modify the list variable in the list:"

print "The old list:"
modifylist=['Xia','Dou']
print modifylist

print "The new list:"
modifylist[0]='Xiao'
print modifylist
print "-----------------------------------"
print "\n"

#
# The tuple is similarity to the list,but tuple don't be allowed to modify !
#
 
tuple = ('Xiao',123,456,'Dou',3.14)
tinytuple = (123,'XiaoDou')
print "This is tuple test:"
print "\n"

print "Show the tuple all data:"
print tuple
print "-----------------------------------"
print "\n"

print "Show the first word of the tuple:"
print tuple[0]
print "-----------------------------------"
print "\n"

print "Show the second word to the forth word of the tuple:"
print tuple[1:3]
print "-----------------------------------"
print "\n"

print "Show the tuple data afer second word:"
print tuple[2:]
print "-----------------------------------"
print "\n"

print "Show the tuple with two times:"
print tinytuple*2
print "-----------------------------------"
print "\n"

print "two tuple links:"
print tuple+ tinytuple
print "-----------------------------------"
print "\n"

print "Show the empty tuple:"
up1 = ()
print up1
print "-----------------------------------"
print "\n"

print "Show the just only one word tuple:"
up2 = ('XiaoDou',)
print up2
print "-----------------------------------"
print "\n"

#
# Set data type test !
#

a = set('123456')
b = set('456789')
print "The collection of a variable have:"
print a
print "-----------------------------------"
print "\n"

print "The collection of b variable have:"
print b
print "-----------------------------------"
print "\n"

print "collection:a-b"
print a-b
print "-----------------------------------"
print "\n"

print "collection:a&b"
print a&b
print "-----------------------------------"
print "\n"

print "collection:a|b"
print a|b
print "-----------------------------------"
print "\n"

print "collection:a^b"
print a^b
print "-----------------------------------"
print "\n"

#
# dictionary data type test !
#

dict = {}
dict['one'] = '1-XiaoDou'
dict['two'] = '2-XiaoDou'

tinydict = {'name':'XiaoDou','site':'XiaoDouTao'}

print "Show the key=one dictionary variable:"
print dict['one']
print "-----------------------------------"
print "\n"

print "Show the key=two dictionary variable:"
print dict['two']
print "-----------------------------------"
print "\n"

print "Show the all dictionary variable of dict:"
print dict
print "-----------------------------------"
print "\n"

print "Show the all key of dict:"
print dict.keys()
print "-----------------------------------"
print "\n"

print "Show the all variables of dict:"
print dict.values()
print "-----------------------------------"
print "\n"

'''
print "Show links from two dicts:"
print dict+tinydict
print "-----------------------------------"
print "\n"
'''
