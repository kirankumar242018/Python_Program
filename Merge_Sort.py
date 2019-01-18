# ****************************** Merge Sort Algorithm Problem  ************************************#
#  Purpose: Solving Merge Sort Algorithm
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */


from Utility import UtilityTest

m1 = UtilityTest.TestFunctional


class Merge_Sort:
    try:
        arr = []
        n = int(input("enter the size of an array \n"))
        print("enter array element \n ")
        for i in range(int(n)):
            n = int(input("enter number: \n"))
            arr.append(int(n))
        print(m1.merge_sort(arr))
    except RuntimeError:
        print("oops something went wrong...\n ")
