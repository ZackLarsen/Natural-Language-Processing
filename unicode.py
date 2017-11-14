#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Zack Larsen, CSC 594 (NLP) HW #2
from __future__ import division
import re, pprint, nltk, sys, datetime, os, collections
from nltk import bigrams, trigrams, word_tokenize, sent_tokenize

from nltk.corpus import inaugural
#print inaugural.fileids()
washington = inaugural.raw('1789-Washington.txt')
jefferson = inaugural.raw('1805-Jefferson.txt')

text = sys.stdin.read()
#print text     #or, print text[:100]


######### Number of sentences ##########
try:
    sent_tokenize_list = sent_tokenize(text)
except:
    #print 'Uh-oh!'
    sent_tokenize_list = sent_tokenize(text.decode('utf-8'))#,'ignore'))


print sent_tokenize_list[:10]
num_sentences = len(sent_tokenize_list)


############### Tokenize ################
tokens = []
for sentence in sent_tokenize_list:
    token_list=word_tokenize(sentence)
    tokens.append(token_list)
print tokens[:4]

#######Add in the <s> and <\s> to the sentence list########
for sentence in tokens:
    sentence.insert(0,'<s>')
    sentence.append('</s>')
print tokens[:4]
print tokens[0][0]

