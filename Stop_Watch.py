""""
*******************************************************************************
*  Purpose : Finding Elapsed Time By Subtracting Start and Stop Time
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

s1 = UtilityTest.TestFunctional()


class Stop_Watch:
    try:
        choice = int(input("enter 1 for start timer\n"))
        while choice != 1:
            choice = int(input("enter valid input\n"))
        start = s1.start(choice)
        print(start)

        choice = int(input("enter 0 for stop timer\n"))
        while choice != 0:
            choice = int(input("enter valid input  \n"))
        s1.stop(choice, start)

    except RuntimeError:
        print("oops something went wrong... \n")
