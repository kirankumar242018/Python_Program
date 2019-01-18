""""
*******************************************************************************
*  Purpose : Finding the Distance From Given X,Y Values
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""


from Utility import UtilityTest

d1 = UtilityTest.TestFunctional


class Distance_Find:
    try:
        x = int(input("enter x values \n"))
        y = int(input("enter y values \n"))
        d1.distance(x, y)
    except RuntimeError:
        print("oops something went wrong....")