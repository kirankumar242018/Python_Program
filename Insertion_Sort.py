# ****************************** Insertion Sort Problem  ************************************#
#  Purpose: Solving Insertion Sort Algorithm
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */


from Utility import UtilityTest

i1 = UtilityTest.TestFunctional


class Insertion_Sort:
    try:
        arr = []
        n = int(input("enter size of an array \n"))
        print("enter array element..\n")
        for i in range(n):
            arr.append(n)
        print(i1.insertion_sort(arr))
        print("======================\n")

        my_list = []
        print("enter array element..\n")
        for i in range(str(n)):
            arr.append(n)
        print(i1.insertion_sort(my_list))

    except RuntimeError:
        print("oops something went wrong \n")
