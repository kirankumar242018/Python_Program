"""
*******************************************************************************
*  Purpose : Generating Distinct Coupon Numbers Using Random Function
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""

from Utility import UtilityTest

c1 = UtilityTest.TestFunctional


class CouponNumbers:
    try:
        no_of_coupons = int(input("enter no_of_coupons needed..\n"))  # taking user input
        while no_of_coupons < 0:  # input validations checking.
            no_of_coupons = int(input("enter positive range values...\n"))  # avoid taking negative values from users
        c1.coupon_generator(no_of_coupons)  # calling function using object reference
    except RuntimeError:          # exception handling
        print("oops something went wrong...\n")
