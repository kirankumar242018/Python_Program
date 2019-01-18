""""
*******************************************************************************
*  Purpose : Finding the Triplets in Given Array
*  @author : KIRAN KUMAR S
*  @Version : 3.7
*  @Since   : 12-01-2019
*
*

"""


from Utility import UtilityTest

k1 = UtilityTest.TestFunctional


class Triplets_Sum:
    try:
        arr = list()
        n = int(input("enter size of an array \n"))
        print("enter array elements..\n")
        for i in range(int(n)):
            n = input("numbers:\n")
            arr.append(int(n))

        k1.triplets(arr)

    except RuntimeError:
        input("oops something went wrong...")