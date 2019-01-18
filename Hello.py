""""
*******************************************************************************
*  Purpose : Demo Program
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""


from Utility import UtilityTest


class HelloWorld:
    h1 = UtilityTest.Test()
    print("Welcome to python")
    name = input("Enter the name")
    h1.dipslay(name)
