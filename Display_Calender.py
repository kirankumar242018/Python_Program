# ******************************************************************#
#  Purpose: Displaying  Calender Using 2D array
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */

from DataStructure_Utility.Utility_DataStructure import Test_LinkedList

l1 = Test_LinkedList()


class Dispaly_Calender:
    try:
        print("enter month....")
        month = int(input())     # taking month as input
        while month <= 0 or month > 12:  # validating
            print("invalid entry....\n")
            month = int(input())  # taking month as input

        print("enter year....\n")
        year = int(input())       # taking years as user input
        while year <= 999 or year > 9999:  # validating
            print("invalid entry....\n")
            month = int(input())   # taking years as user input

        l1.displayCalOfMonth(month, year)  # calling method

    except ValueError:  # handling exceptions
        print("==oops something went wrong,please give valid inputs...\n")
