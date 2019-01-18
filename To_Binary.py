from Utility import UtilityTest
b1 = UtilityTest.TestFunctional


class To_Binary:
    try:

        print("enter numbers \n")
        num = int(input())
        str1 = b1.decimalToBinary(num).replace("0b"," ")
        print(str1)
        b1.toBinary(str1)

    except RuntimeError:
        print("oops something went wrong\n")