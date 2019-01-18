""""
*******************************************************************************
*  Purpose : Replace <<USER NAME>> By User Input Names(String)
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

p1 = UtilityTest.TestFunctional()


class UserName:
    try:
        name = input("enter username\n")  # taking users inputs
        while len(name) <= 3 or name.isdigit():  # input validation
            name = input("please provide valid name\n") # taking user inputs
        p1.username(name)  # passing the arguments to the functions

    except RuntimeError:  # handling exception
        print("exception raised")
