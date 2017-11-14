#!/usr/bin/python
#Zack Larsen, CSC 594 (NLP)

import sys, datetime
import re
import nltk
from nltk.tokenize import sent_tokenize
import os
import codecs

data = sys.stdin.read().encode('utf8')

print data
text = data
######### Number of words (tokens) ##########
text = re.sub(r'\'m', " am", text) #I am
text = re.sub(r'n\'t', " not", text) #Do not
text = re.sub(r'\'ve', " have", text) #They've to they have
text = re.sub(r'\'re', " are", text) #they're to they are
text = re.sub(r'\'ll', " will", text) #They'll to they will
text = re.sub(r'\'d', " would", text) #They'd to they would

print text
