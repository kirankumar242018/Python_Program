# ****************************** Bubble Sort Algorithm  ************************************#
#  Purpose: Solving Bubble Sort Algorithm
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */


from Utility import UtilityTest

b1 = UtilityTest.TestFunctional


class Bubble_Sort:
    try:
        """=======Integer array==="""
        arr = []
        n = int(input("enter size of an array \n"))
        print("enter array elements..\n")
        for i in range(int(n)):
            x = input()
            arr.append(x)
        print(b1.bubble_sort(arr))

        """=======String array==="""
        my_list = []
        print("enter array elements..\n")
        for i in range(n):
            y = input()
            my_list.append(y)
        print(b1.bubble_sort(my_list))

    except RuntimeError:
        print("oops something went wrong....")
