""""
*******************************************************************************
*  Purpose : Finding the Harmonic Values of Given Numbers
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

h1 = UtilityTest.TestFunctional


class Harmonic:
    try:
        n=int(input("enter the number to check harmonic..\n"))
        if n != 0:
            h1.harmonic(n)
        else:
            print("invalid input")
    except RuntimeError:
        print("oops something went wrong....")