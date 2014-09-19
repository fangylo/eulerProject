import os
import sys
import re

def problem_1():
    x=0
    for i in range(0,1000):
        if (i%3==0) or (i%5==0):
            x+=i
    return x
    
if __name__ == '__main__':
    problem_1()
    
    print problem_1()
