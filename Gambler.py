""""
*******************************************************************************
*  Purpose : solving the Gambler Algorithm Using Random Methods
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

g1 = UtilityTest.TestFunctional()


class Gambler:
    try:
        stake = int(input("enter stack amount\n"))
        goals = int(input("enter goals amount\n"))
        no_of_times = int(input("enter no_of_times\n"))
        g1.gambler(stake, goals, no_of_times)

    except RuntimeError:
        print("oops something went wrong..\n")
