#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Zack Larsen, CSC 594 (NLP) HW #2
from __future__ import division
import re, pprint, nltk, sys, datetime, os, collections
#from nltk.probability import *
from nltk import bigrams, trigrams, word_tokenize, sent_tokenize, corpus

#text = sys.stdin.read()
#print text     #or, print text[:100]


from nltk.corpus import inaugural
#print inaugural.fileids()
washington = inaugural.raw('1789-Washington.txt')
jefferson = inaugural.raw('1805-Jefferson.txt')

print washington
