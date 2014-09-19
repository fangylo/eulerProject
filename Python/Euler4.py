import math
import time

# def isPalindrome(n):
    # """ (int) -> (Bool)"""
    # if n < 10:
        # return True
    # else:
        # listOfDigits = [];
        # newNumerator = n;
        # count = 0
        # while newNumerator/10 > 0:
            # remainder = newNumerator%10;
            # newNumerator = newNumerator/10;
            # listOfDigits.append(remainder);

            # count = count+1;
        # # The last digit:
        # remainder = newNumerator%10;      
        # listOfDigits.append(remainder);
        # reversedDigits = []
        # for j in reversed(listOfDigits):
            # reversedDigits.append(j)
        # if reversedDigits== listOfDigits:
            # return True
        # else:
            # return False
        
def isPalindrome(n):
    """ (int) -> (Bool)"""
    if str(n) == str(n)[::-1]: return True
    else : return False

def findMaxPalindrome():
    """ (int) -> (int)"""
    palindromeList=[];
    # maxPalindromeNumber = 0;

    for i in range(1000,100,-1):
        for j in range(1000,100,-1):
            if i>= j:
                product = i*j;
                if isPalindrome(product): 
                    palindromeList.append(product);
                    # if product >= maxPalindromeNumber:
                        # maxPalindromeNumber = product;
    result = max(palindromeList)
    # result = maxPalindromeNumber;
    return result
                
    
    
    
if __name__ == '__main__':
    # largestPrimeFactor(100)
    start = time.time()
    result = findMaxPalindrome()
    end = time.time()
    elapsed = (end  - start)

    print "result %s returned after %s seconds." % (result, elapsed)
