#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "nmd17"

import sys

openBrackets = ["(", "<", "(*", "{", "["]
closedBrackets = [")", ">", "*)", "}", "]"]

def my_function(string):
    temp1 = []
    tempIndex = []
    index = 0

    while string:
        if len(string) > 1:
            if string[0] + string[1] in openBrackets:
                tempIndex.append(openBrackets.index(string[0] + string[1]))
                temp1.append(string[0] + string[1])
                string = string[2:]
                index += 1
             
            elif string[0] in openBrackets:
                tempIndex.append(openBrackets.index(string[0]))
                temp1.append(string[0])
                string = string[1:]
                index += 1
           
            elif string[0] + string[1] in closedBrackets:
                if tempIndex[-1] == closedBrackets.index(string[0] + string[1]):
                    temp1.pop()
                    tempIndex.pop()
                    string = string[2:]
                    index += 1
                else:
                    break
               
            elif string[0] in closedBrackets:
                if tempIndex[-1] == closedBrackets.index(string[0]):
                    temp1.pop()
                    tempIndex.pop()
                    string = string[1:]
                    index += 1
                else:
                    break
                   
            elif string[0] not in openBrackets and string[0] not in closedBrackets:
                string = string[1:]
                index += 1

        elif len(string) == 1:
            if string[0] in openBrackets:
                temp1.append(string[0])
                string = string[1:]
                index += 1

            elif string[0] in closedBrackets:
                if tempIndex[-1] == closedBrackets.index(string[0]):
                    temp1.pop()
                    tempIndex.pop()
                    string = string[1:]
                    index += 1
                else:
                    break
                        
            elif string[0] not in closedBrackets and string[0] not in openBrackets:
                string = string[1:]
                index += 1
        
    if len(temp1) == 0:
        print("YES")
    else:
        print("NO" + " " + str(index + 1))



    

def main(args):
    """Add your code here"""
    if len(args) != 2:
        print('usage: python nested.py file-to-read')
        sys.exit(1)
    print(args)
    with open(args[1], 'r') as f:
        contents = f.read()
        contentsTemp = contents.split("\n")
        for line in contentsTemp:
            print(line)
            print(my_function(line))


if __name__ == '__main__':
    main(sys.argv)
