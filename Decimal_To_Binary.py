from Utility import  UtilityTest
d1 = UtilityTest.TestFunctional


class Decimal_to_binary:
    try:
        print("enter numbers \n")
        num = int(input())
        d1.decimalToBinary(num)
    except RuntimeError:
        print("oops something went wrong....\n")
