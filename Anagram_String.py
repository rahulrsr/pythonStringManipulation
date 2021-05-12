#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def get_freq(a):
    dict = {}
    for item in a:
        dict[item] = a.count(item)
    return dict


def makeAnagram(a, b):
    a = sorted(a)
    len_a = len(a)
    b = sorted(b)
    len_b = len(b)
    a_dict = get_freq(a)
    b_dict = get_freq(b)
    a_key = a_dict.keys()
    b_key = b_dict.keys()
    a_key = set(a_key)
    b_key = set(b_key)
    diff1 = a_key - b_key
    diff2 = b_key - a_key
    count_a = 0
    count_b = 0
    if len(diff1) > 0:
        #count_a = 0
        for v in diff1:
            count_a += int(a_dict[v])
    if len(diff2) > 0:

        for v in diff2:
            count_b += int(b_dict[v])
    common_elements=a_key.intersection(b_key)
    count_common=0
    if len(common_elements)>0:
        for v in common_elements:
            if a_dict[v]==b_dict:
                continue
            else:
                c=int(a_dict[v])-int(b_dict[v])
                if c>0:
                    count_common+=c
                else:
                    c=c*(-1)
                    count_common+=c


    return count_a + count_b+count_common


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    #fptr.write(str(res) + '\n')

    #fptr.close()
    print(res)
