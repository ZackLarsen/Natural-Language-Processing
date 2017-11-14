#!/usr/bin/python 
#Zack Larsen, CSC 594 (NLP)
import re
import nltk
from nltk.tokenize import sent_tokenize

data = 'data-medium.txt'

######### Number of paragraphs  ##########
def paragraph_count(infile):
    f = open(infile, 'r')
    linecount = 0
    paragraphcount = 0
    empty = True
    for i in f:
        if '\n' in i:
            linecount += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraphcount = paragraphcount + 1
                empty = False
    print '# of paragraphs = ',paragraphcount
    f.close()

paragraph_count(data)

######### Number of sentences ##########
text = open(data).read()
#print text
sent_tokenize_list = sent_tokenize(text)
#print sent_tokenize_list
#print len(sent_tokenize_list)
num_sentences = len(sent_tokenize_list)
print '# of sentences = ',num_sentences

######### Number of words (tokens) ##########
tokens = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*",text)
#print tokens
token_count = len(tokens)
print '# of tokens = ',token_count

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
