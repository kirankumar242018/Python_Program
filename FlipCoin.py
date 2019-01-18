""""
*******************************************************************************
*  Purpose : Solving Flip Coins Using Random Methods
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

f1 = UtilityTest.TestFunctional()


class FlipCoin:
    try:
        n = int(input("enter number to flip a coin \n"))  # taking users inputs
        if n < 0:
            print("enter number above 0\n")  # avoid negative values
        else:
            f1.flipcoin(n)  # if input is positive accept it
    except RuntimeError:
        print("oops something went wrong...\n")  # if exception occurs
