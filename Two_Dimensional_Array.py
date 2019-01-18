""""
*******************************************************************************
*  Purpose : Performing Two Dimensional Array
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

t1 = UtilityTest.TestFunctional


class Two_Dimensional_Array:
    try:
        rows = int(input("enter row number"))
        cols = int(input("enter column number"))
        t1.two_dimensional_array(rows, cols)
    except RuntimeError:
        print("oops something went wrong...")