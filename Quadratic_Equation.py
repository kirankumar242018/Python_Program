""""
*******************************************************************************
*  Purpose : Performing the Quadratic Equation Using Formula
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

q1 = UtilityTest.TestFunctional


class Quadratic_Equation:
    try:
        a = int(input("enter value for a..\n"))
        b = int(input("enter value for b..\n"))
        c = int(input("enter value for c..\n"))
        q1.quadratic_equation(a, b, c)
    except ZeroDivisionError:
        print("oops something went wrong divide by zero exceptions raised....")