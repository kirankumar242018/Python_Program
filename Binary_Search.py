# ****************************** Binary Search Problem  ************************************#
#  Purpose: Solving Binary Search Algorithm
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */


from Utility import UtilityTest

b1 = UtilityTest.TestFunctional


class Binary_Search:
    try:
        arr = list()
        n = int(input("enter a array size...\n"))
        print("enter array element...\n")
        for i in range(n):
            arr.append(input())
        key = input("enter key to search element in given array..\n")
        if key in arr:
            print("key found at position..=> ", b1.binary_search(arr, key))
        else:
            print("entered element not found sorry...\n")
        print("===========================")

        my_list = list()
        print("enter array element...\n")
        for i in range(n):
            my_list.append(input())
        key = str(input("enter key to search element in given array..\n"))
        if key in my_list:
            print("key found at position..=> ", b1.binary_search(my_list, key))
        else:
            print("entered element not found sorry... \n")

    except RuntimeError:
        print("oops something went wrong...")
