#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Zack Larsen, CSC 594 (NLP) HW #2
from __future__ import division
import re, pprint, nltk, sys, datetime, os, collections, shelve
from nltk import bigrams, trigrams, word_tokenize, sent_tokenize
import math

#text = sys.stdin.read()
#print text     #or, print text[:100]

b = shelve.open('bigrams.db')
bigrams = b['bigrams']
b.close()
#print bigrams

u = shelve.open('unigrams.db')
#print u.keys()
unigrams = u['unigrams']
u.close()
#print unigrams


w = shelve.open('wordtypes.db')
wordtypes = w['wordtypes']
w.close()



print sum(wordtypes.values())


#print 'average', sum(wordtypes.values())/len(wordtypes)
