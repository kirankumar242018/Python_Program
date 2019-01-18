from Utility import UtilityTest

m1 = UtilityTest.TestFunctional


class Monthly_Payment:
    try:
        p = int(input("enter principale \n"))
        y = int(input("enter year \n"))
        r = float(input("enter rate of interest \n "))
        m1.monthlyPayment(p, y, r)
    except RuntimeError:
        print("oops something wents wrong...\n")