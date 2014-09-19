import os
import sys
import re


def fibonacciGenerator(max):
  """ (int) ->  list of int"""
  if max < 3:
    raise Exception("input value needs to be >= 3")
  result = [1,2]
  num1 = 1
  num2 = 2
  while (num1+num2) <= max:
    nextNumber = num1 + num2
    num1 = num2
    num2 = nextNumber
    result.append(num2)
  return result
  
def sumOfEvenNumbers(listOfNumbers):
  """ list of int -> int"""
  total = 0
  for number in listOfNumbers:
    if (number %2)==0:
      total+= number
  return total
    

  
if __name__ == '__main__':
     # print fibonacciGenerator(10)
    print sumOfEvenNumbers(fibonacciGenerator(4000000))
