#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Zack Larsen, CSC 594 (NLP) HW #2
from __future__ import division
import re, pprint, nltk, sys, datetime, os, collections, shelve
from nltk import bigrams, trigrams, word_tokenize, sent_tokenize
import math

text = sys.stdin.read()
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


#### Calculate the average probability of a word for use in cases where the token is truly 'unknown' ####
average_count = sum(wordtypes.values())/len(wordtypes)
default_prob = average_count / len(wordtypes)

######### Number of sentences ##########
sent_tokenize_list = sent_tokenize(text)
#print sent_tokenize_list[0]
#############Generate N-grams on the test set sentences##############
def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

N = 131366

###############################################################################################
############## For each sentence in test set, compute probability using chain rule ############
for i in range(0,len(sent_tokenize_list)):
    #tokenize the sentence
    token_list=word_tokenize(sent_tokenize_list[i])
    token_list.insert(0,'<s>')
    token_list.append('</s>')
    #print token_list

    #create the unigrams and bigrams from the sentence
    bigram_list = find_ngrams(token_list,2)
    #print bigram_list
    unigram_list = token_list


    #compute probability by taking ln(sumPR), where sumPR is the sum of the probabilities of the tokens in the sentence.
    #convert this later using exp(ln(sumPR))
    bigramsum = 0
    for bigram in bigram_list:
        if bigram in bigrams:
            prob = bigrams[bigram]
            #print prob
            bigramsum += math.log(prob)
        else:  #If it was not in the training set of bigrams, we will have to calculate probability using wordtypes.db
            if bigram[0] in wordtypes and bigram[1] in wordtypes:
                firstprob = wordtypes[bigram[0]] / sum(wordtypes.values()) 
                secondprob = wordtypes[bigram[1]] / sum(wordtypes.values())
                prob =  firstprob*secondprob
                bigramsum += math.log(prob)
            else:
                prob = default_prob
                bigramsum += math.log(prob)
    bigramprob = math.exp(bigramsum)
    #print bigramprob
    # To compute perplexity, we just take the probability raised to the pwer of (-1/N)
    try:
        bigram_perplexity = bigramprob**(-1/N) 
    except:
        bigram_perplexity = 'Error in computation'

    unigramsum = 0
    for unigram in unigram_list:
        if unigram in unigrams:
            prob = unigrams[unigram]
            unigramsum += math.log(prob)
        elif unigram in wordtypes:
            prob = wordtypes[unigram]
            unigramsum += math.log(prob)
        else:
            prob = default_prob
            unigramsum += math.log(prob)
    unigramprob = math.exp(unigramsum)
    try:
        unigram_perplexity = unigramprob**(-1/N)
    except:
        unigram_perplexity = 'Error in computation'

    print 'N is:',N
    print 'Sentence',i,':', sent_tokenize_list[i]
    print '-unigram [Prob]',unigramprob, '[Perp]',unigram_perplexity
    print '-bigram  [Prob]',bigramprob, '[Perp]',bigram_perplexity
    print '\n'














#####################################################################################################
###########Create a bigram probability dictionary using ALL wordtypes that do not appear in the training data########
#bgwtcounts = {}
#for bigram in bigrams:
#    bgwtcounts[bigram] = bgwtcounts.get(bigram,0)+1
#bgwttotal = sum(bgwtcounts.values())
#print 'Total number of unique bigrams = ',len(bigramcounts)
#############Store bigram wordtypes probabilities in a dictionary#############
#bgwt_probs = {}
#for bigram in bigrams:
#    bgwt_probs[bigram] = bgwtcounts[bigram]/bgwttotal
#####################################################################################################


