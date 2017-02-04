#!/usr/bin/env python
# made by siddharth sharma
# further work include making this a standalone app
# type python vocabbuilder.py to run in terminal

#for installing pip:  sudo apt-get install python-pip
import easygui #sudo apt-get install python-easygui, sudo apt-get install python-tk
import time
import xlrd  #sudo apt-get install python-xlrd
import random
import sys
import pyttsx #sudo pip install pyttsx


def popup(word):
	title = "Vocabbuilder by Siddharth Sharma"
	temp = easygui.indexbox(word,title,('continue','speak','exit')) 
	if temp == 2:
		quit()
	if temp == 1:
		engine.say(word)
		engine.runAndWait()
		popup(word)	

engine = pyttsx.init()


book = xlrd.open_workbook("wordlist.xls")
first_sheet = book.sheet_by_index(0)

msg = "Enter information"
title = "Vocabbuilder by Siddharth Sharma"
fieldNames = ["Start range","End range","Time between words in min"]
fieldValues = [] 
fieldValues = easygui.multenterbox(msg,title, fieldNames)

while 1:
	errmsg = ""
	if fieldValues == None:
		quit()
	for i in range(len(fieldNames)):
		if fieldValues[i].strip() == "":
			errmsg = errmsg + ('"%s" is a required field.' % fieldNames[i])
	if errmsg == "": break
	fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)

while 1:
	rand = random.randrange(int(fieldValues[0]), int(fieldValues[1]), 1) 
	word = first_sheet.row_values(rand)[0] + " : " + first_sheet.row_values(rand)[1]
	popup(word)
	time.sleep(float(fieldValues[2])*60)
