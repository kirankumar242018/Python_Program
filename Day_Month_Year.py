# ****************************** Printing Day_Month_Year Problem  ************************************#
#     Purpose: Printing Day_Month_Year Problem Using Formula
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
#

from Utility import UtilityTest

d1 = UtilityTest.TestFunctional


class Day_Month_Year:
    try:
        d = int(input("enter date\n"))
        m = int(input("enter month\n"))
        y = int(input("enter year\n"))
        d1.day_of_week(d, m, y)
    except RuntimeError:
        print("oops something went wrong \n")
