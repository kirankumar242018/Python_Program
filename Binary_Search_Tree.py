# ******************************************************************#
#  Purpose: Solving Binary Search Problem Using formula
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   23-01-2019
#
# */


from DataStructure_Utility.Utility_DataStructure import Test_LinkedList

l1 = Test_LinkedList()


class Binary_Search_Tree:
    try:
        print("enter a number to implement binary search tree....\n")
        num = int(input())

        var1 = l1.binary_search_tree(num)       # n! factorial
        var2 = l1.binary_search_tree(num * 2)   # (num * 2)!
        var3 = l1.binary_search_tree(num+1)     # (num+1)!
        result = var3 * var1                    # (num+1)! * (n)!
        divisor = var2 // result
        print(divisor)
    except ValueError:
        print("oops something went wrong.....\n")