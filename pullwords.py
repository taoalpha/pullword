import sys
import codecs
import re
import collections
#import pyPdf


def coded(filename):
    sentence = []
    try:
        f = codecs.open(filename, "r", encoding="utf-16")
        for line in f:
            sentence.append(line)
    except UnicodeError:
        f = open(filename, "r")
        for line in f:
            sentence.append(line)
    #for line in codecs.open(filename, "r", encoding="utf-16").readlines():
    #    if line != "\r\n" and line != "111\r\n":
    #        sentence.append(line)
    return sentence


def init(filename, alpha):
    sentence = coded(filename)
    sent1 = []
    word0 = []
    word_a = []
    for li in sentence[:]:
        if not(li.startswith("00")):
            sent1.append(li)
    for li in sent1[:]:
        li = re.sub('[,.!?":\[\];()]', " ", li)
        for wds in li.split():
            word0.append(wds)
    for words in word0[:]:
        if words.startswith(alpha) or words.startswith(alpha.upper()):
            words = words.lower()
            word_a.append(words)
    word_c = collections.Counter(word_a)
    word_a = word_c.most_common(1000000000)
    word_a.sort()
    print "The words starting with %r in %r list below:" % (alpha, filename)
    for word, count in word_a:
        print "{0:<20s}: {1:>8d}".format(word, count)
    #print "\n".join('%s %s' % (x, y) for x in word_c.keys() for y in word_c.values())
    #word_a = list(set(word_a))
    #print "\n".join(word_c)


#def fftype(ffname):


if __name__ == '__main__':
    #convert_to_utf8(sys.argv[1])
    if len(sys.argv) == 3:
        init(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 2:
        alpha = raw_input(">>Please input the character you want to pull the words start with:")
        init(sys.argv[1], alpha)
