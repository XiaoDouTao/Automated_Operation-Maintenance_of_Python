#!/usr/bin env python
#coding:utf-8

'''
================================================================



 Describe: file of python

 Author: XiaoDou

 Update time: Apr/11/2017

 Development environment: CentOS 6.5/python 2.7.12



================================================================
'''


#================================================================
#
#	Read all of the file
#
#================================================================

# you must be create a file is named 'Write_File.txt' and write 
# some words in it,whether the will be error.
Read_File = 'Read_File.txt'

#print "Read all of the file with file.read()\n"
#
#with open(Read_File) as file:
#	contents = file.read()
#	print contents
#
#print "---------------------------------------"
#
#
#print "Read all of the file with line\n"
#with open(Read_File) as file:
#	for line in file:
#		print line.rstrip()


#print "Read all of the file and writed to the list\n"
#
#with open(Read_File) as file:
#	lines = file.readlines()
#	#print lines
#
#for line in lines:
#	print line.rstrip()
#print "---------------------------------------"


with open(Read_File) as file:
	lines = file.readlines()
	
string = ''

for line in lines:
	string += line.rstrip()

print "\nShow the string of file:\n"+string
print "The string length: "+str(len(string))	

print "---------------------------------------"



#================================================================
#
#	Write to the file
#
#================================================================

print "\nWrite to file test:"

# if the file 'Write_File.txt' not be created ,this file will be 
# create automatic
Write_File = 'Write_File.txt'

with open(Write_File,'w') as file:
	file.write('Hello,World!\n')

print "Write to file finish.....\n"


with open(Write_File,'a') as file:
	file.write('This is add string...\n ')

print "Add string to the file finish..."

print "---------------------------------------"
