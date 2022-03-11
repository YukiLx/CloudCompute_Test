#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author：Yuki
@Time：2022/3/11 6:46 下午
@Desc: 
"""
import time
import re

start = time.process_time()
'''function：Calculate the word frequency of each line
    input:  line : a list contains a string for a row
            counts: an empty  dictionary 
    ouput:  counts: a dictionary , keys are words and values are frequencies
    data:2018/10/22
'''


def ProcessLine(line, counts):
    # Replace the punctuation mark with a space

    line = re.sub('[^a-z]', '', line)
    for ch in line:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def main():
    file = open("./a.txt", 'r')
    wordsCount = 0
    alphabetCounts = {}
    for line in file:
        alphabetCounts = ProcessLine(line.lower(), alphabetCounts)
    wordsCount = sum(alphabetCounts.values())
    alphabetCounts = sorted(alphabetCounts.items(), key=lambda k: k[0])
    alphabetCounts = sorted(alphabetCounts, key=lambda k: k[1], reverse=True)
    for letter, fre in alphabetCounts:
        print("|\t{:15}|{:<11.2%}|".format(letter, fre / wordsCount))

    file.close()


if __name__ == '__main__':
    main()

end = time.process_time()
print("RunTime=%s"%(end - start))