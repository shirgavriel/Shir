# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:24:39 2019

@author: שיר גבריאל
makes a dictionary with 3 keys,values and a string
print yes if string in dict, no others
"""

def dict():
    dict = {}
    for x in range (3):
        key = input("please enter the key ")
        dict [key] = int(input("please enter the value (an integer number) "))
    return dict

def ifKeyInDict(dict):
    str = input("please enter a key string ")
    if str in dict:
        print ("yes")
    else:
        print("no")
    

def main():
    x = dict()
    ifKeyInDict(x)
    
    
if __name__ == '__main__':
    main()
    

