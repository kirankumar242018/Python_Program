# ****************************** Vending_Machine Problem  ************************************#
#  Purpose: Vending_Machine Problem
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
#

from Utility import UtilityTest

v1 = UtilityTest.TestFunctional


class Vending_Machine:
    try:
        money = int(input("enter the money values\n"))
        notes = [1000, 500, 100, 50, 20, 10, 5, 1]
        v1.vending_machine(money, notes)
    except RuntimeError:
        print("oops something went wrong .....\n")
