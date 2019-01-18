""""
*******************************************************************************
*  Purpose : Programing Wind-Chill With User Input Temprature as T and Wind Speed as V
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

w1 = UtilityTest.TestFunctional


class Wind_Chill:
    try:
        temp = int(input("enter temprature in fahrenheit...\n"))
        wind_speed = int(input("enter wind speed in miles per hour..\n"))
        w1.wind_chill(temp, wind_speed)
    except RuntimeError:
        print("oops something went wrong...\n")