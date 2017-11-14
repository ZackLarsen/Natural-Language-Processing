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
data = sys.stdin.read()
#print data
    
######### Number of paragraphs  ##########
def paragraph_count(infile):
    #f = open(infile, 'r')
    linecount = 0
    paragraphcount = 0
    empty = True
    for i in infile:   #f
        if '\n' in i:
            linecount += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraphcount = paragraphcount + 1
                empty = False
    print '# of paragraphs = ',paragraphcount
    #f.close()

paragraph_count(data)

######### Number of sentences ##########
#text = open(data).read()
#print text

text = data
sent_tokenize_list = sent_tokenize(text)
#print sent_tokenize_list
#print len(sent_tokenize_list)
num_sentences = len(sent_tokenize_list)
print '# of sentences = ',num_sentences

######### Number of words (tokens) ##########
text = re.sub(r'\'m', " am", text) #I am
text = re.sub(r'n\'t', " not", text) #Do not
text = re.sub(r'\'ve', " have", text) #They've to they have
text = re.sub(r'\'re', " are", text) #they're to they are
text = re.sub(r'\'ll', " will", text) #They'll to they will
text = re.sub(r'\'d', " would", text) #They'd to they would

#print text

tokens = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*",text)
#print tokens

# Now, we just need to add the part to deal with personal pronouns
personal_pronouns = ['he\'s','He\'s','she\'s','She\'s','it\'s','It\'s']

for token in tokens:
    if token in personal_pronouns:
        re.sub(r'\'s', " is", token)
        

token_count = len(tokens)
print '# of tokens = ',token_count

#print tokens

######### Number of types ##########
already_seen = {}
for token in tokens:
    if token in already_seen:
        already_seen[token] += 1
    else:
        already_seen[token] = 1

sorted_tokens = sorted(already_seen.items(), key=lambda x: x[0])    # ,reverse = True)
print '# of types = ',len(sorted_tokens)
print '#################################'

######## Printing out ##########
#for token in sorted_tokens:
#    print token[0],token[1]

newsort = [v for v in sorted(already_seen.items(), key=lambda(k,v): (-v,k))]
for item in newsort:
    print item[0],item[1]
