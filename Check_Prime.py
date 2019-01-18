# ****************************** Finding Prime Numbers Problem  ************************************#
#  Purpose: Solving Prime Numbers Algorithm
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */



from Utility import UtilityTest

p1 = UtilityTest.TestFunctional


class Check_Prime:
    try:
        start = int(input("enter start range...\n"))
        end = int(input("enter peak range...\n"))
        p1.is_prime(start, end)
    except RuntimeError:
        print("oops something went wrong...\n")
