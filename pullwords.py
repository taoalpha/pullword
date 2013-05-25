#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import re
# import collections
#import pyPdf


def coded(filename):
    sentence = []
    try:
        f = codecs.open(filename, "r", encoding="utf-16")
        strs = f.read()
        sentence = re.findall("\w+", str.lower(strs))
        # for line in f:
        #     sentence.append(line)
    except UnicodeError:
        f = open(filename, "r")
        strs = f.read()
        sentence = re.findall("\w+", str.lower(strs))
        # for line in f:
        #     sentence.append(line)
    #for line in codecs.open(filename, "r", encoding="utf-16").readlines():
    #    if line != "\r\n" and line != "111\r\n":
    #        sentence.append(line)
    return sentence


def removeNonAscii(s):
    return ("".join(filter(lambda x: ord(x) < 128 and ord(x) > 64, s)))


def compared(word_l):
    # word_l = []
    # for word, count in words:
    #     word_l.append(word)
    try:
        for i in range(len(word_l)):
            if len(word_l[i]) > 2:
                wordf = word_l[i]
                for word in word_l[i + 1:i + 10]:
                    if word.startswith(wordf) and (len(word) - len(wordf)) < 4:
                        word_l.remove(word)
    except:
        pass
    return word_l


def init(filename, alpha):
    sentence = coded(filename)
    sent1 = []
    word0 = []
    word_a = []
    # for li in sentence[:]:
    #     if not(li.startswith("00")):
    #         sent1.append(li)
    for li in sentence[:]:
        li = re.sub('[-,,.!?":\[\]\';()~]', " ", li)
        wds = removeNonAscii(li)
        if len(wds) > 3 and not wds.startswith("aa"):
            word0.append(wds)
    for words in word0[:]:
        if words.startswith(alpha) or words.startswith(alpha.lower()):
            word_a.append(words)
    # word_c = collections.Counter(word_a)
    # word_a = word_c.most_common(1000000000)
    word_a = list(set(word_a))
    word_a.sort()
    word_a = compared(word_a)
    # for i in range(len(word_a)):
    #     word_a = compared(word_a)
    print "The words starting with %r in %r list below:" % (alpha, filename)
    for word in word_a:
        print "{0:<20s}: {1:>8d}".format(word, sentence.count(word))


# def fftype(ffname):


if __name__ == '__main__':
    #convert_to_utf8(sys.argv[1])
    if len(sys.argv) == 3:
        init(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 2:
        alpha = raw_input(">>Please input the character \
            you want to pull the words start with:")
        init(sys.argv[1], alpha)
