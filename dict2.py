# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:21:51 2019

@author: שיר גבריאל
for nums from 0-4 key=num,value=num**2
"""


def dict():
    dict = {}
    for x in range (5):
        dict[x] = x**2
    return dict

def main():
    x=dict()
    print (x)


if __name__ == '__main__':
    main()