from Utility import  UtilityTest
s1 = UtilityTest.TestFunctional


class Squareroot_Newton:
    try:
        num = int(input("enter the numbers to find square root \n"))
        s1.sqrt(num)
    except RuntimeError:
        print("oops something went wron \n")
