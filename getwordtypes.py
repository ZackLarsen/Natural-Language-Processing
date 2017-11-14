#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Zack Larsen, CSC 594 (NLP) HW #2
from __future__ import division
import re, pprint, nltk, sys, datetime, os, collections, shelve
from nltk import bigrams, trigrams, word_tokenize, sent_tokenize
import math
import shelve

#text = sys.stdin.read()
#print text     #or, print text[:100]


c = shelve.open('wordtypes.db')
wordtypes = c['wordtypes']
c.close()

print wordtypes
