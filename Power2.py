""""
*******************************************************************************
*  Purpose : Prints the Power of 2 for Given integer numbers
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

t1 = UtilityTest.TestFunctional


class Power2:
    try:
        n = int(input("enter the numbers..\n"))
        if n > 1 and n < 32:
            t1.power2(n)
        else:
            print("invalid input...\n")
    except RuntimeError:
        print("oops something went wrong...\n")
