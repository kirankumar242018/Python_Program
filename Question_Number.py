import math

from Utility import UtilityTest

q1 = UtilityTest.TestFunctional


class Question_Number:
    try:
        no_of_times = int(input("enter to check number of time \n"))
        low = 0
        high = int(math.pow(2,no_of_times))
        print("the number between(", low, ") to(", high, ") in range\n")
        res=q1.question_number(low, high)
        print(res)
    except RuntimeError:
        print("oops something went wrong \n")