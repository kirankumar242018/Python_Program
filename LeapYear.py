""""
*******************************************************************************
*  Purpose : Checking Leap Year For Given Input Values
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""


from Utility import UtilityTest

l1 = UtilityTest.TestFunctional()


class LeapYear:
    try:

        year = int(input("enter input to check leap year and should 4 digit"))

        if (year > 1000 and year < 9999):  # checking the range between 1000 to 9999
            l1.leapyear(year)

        else:  # else part
            print("enter valid input")


    except RuntimeError:  # exception handling
        print("oops something went wrong")
