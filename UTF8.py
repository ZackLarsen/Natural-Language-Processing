
#!/usr/bin/python
#Zack Larsen, CSC 594 (NLP)

import sys, datetime
import re
import nltk
from nltk.tokenize import sent_tokenize
import os
import codecs


UTF8Reader = codecs.getreader('utf8')
sys.stdin = UTF8Reader(sys.stdin)
data = sys.stdin.read()

#data = codecs.open(data, "r", "utf-8")


