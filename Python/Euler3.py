import math
import time


def largestPrimeFactor(n):
    """ (int) -> (int)"""
  
    largestFactor = 1
    numberToCheck = n
    
    maxNumber = int(math.ceil(math.sqrt(numberToCheck)))
    newMaxNumber = maxNumber

    for i in range(2, maxNumber+1):
      
      if i > newMaxNumber:
        break
      while numberToCheck % i == 0:
        largestFactor = i
        numberToCheck = numberToCheck/i
        newMaxNumber  = int(math.ceil(math.sqrt(numberToCheck)))
        print "i=" + str(i)
        print "numberToCheck=" + str(numberToCheck)
        print "newMaxNumber=" + str(newMaxNumber)
        print "numberToCheck/i = " + str(numberToCheck/i)
 
    if  numberToCheck > largestFactor:
      largestFactor = numberToCheck
    return largestFactor

# def lpf(inputNum):    
    # count = 1    
    # numberToCheck = int(math.floor(math.sqrt(inputNum)))
    # i = inputNum
    # while i > numberToCheck:
        # i = i - 1 
        # count = count + 1                
        # if inputNum % i == 0:          
          # largeFactor = lpf(i)
          # return  largeFactor
            
    # return inputNum    
    
if __name__ == '__main__':
  # largestPrimeFactor(100)
  start = time.time()
  result = largestPrimeFactor(600851475143)
  elapsed = (time.time() - start)
  print "result %s returned after %s seconds." % (result, elapsed)
