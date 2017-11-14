#!/usr/bin/python
#Zack Larsen, CSC 594 (NLP)

import sys, datetime
import re
import nltk
from nltk.tokenize import sent_tokenize
import os

#os.chdir('/Users/zacklarsen/Desktop/CSC 594/HW/HW #1')
#data = 'data-medium.txt' #This allows us to specify the input file
#This uses standard input so that we can specify the text file in the command line
#with open(sys.argv[1], 'r') as f:
#    contents = f.read()
#print contents

text = sys.stdin.read()
print text

#import fileinput
#for line in fileinput.input():
#    print(line)
