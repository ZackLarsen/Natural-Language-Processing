#!/usr/bin/python

text = open('data-small.txt').read()


def insert_line_para_nums(infile):
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
            if empty is True:
                paragraphnumber = 0
            else:
                paragraphnumber = paragraphcount

    print paragraphcount
    f.close()



insert_line_para_nums('data-small.txt')
