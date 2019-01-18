""""
*******************************************************************************
*  Purpose : Solving the String Permutation Problem
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

s1 = UtilityTest.TestFunctional


class String_Permutation:
    try:
        string = str(input("enter string to check permutation \n"))
        print(s1.permutation(string))
    except RuntimeError:
        print("oops something went wrong....\n")
