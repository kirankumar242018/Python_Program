"""
*******************************************************************************
*  Purpose : Consider a Prime Factorization of N Using Brute Force
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""


from Utility import UtilityTest

f1 = UtilityTest.TestFunctional()


class Factorization:
    try:
        n = int(input("enter number to find factor...\n"))
        if n > 1:
            f1.primefact(n)
        else:
            print("give number above 1...\n")
    except RuntimeError:
        print("oops something went wrong...\n")
