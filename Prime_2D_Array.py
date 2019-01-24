# ******************************************************************#
#  Purpose: Displaying Prime Numbers in 2D Array
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */

from DataStructure_Utility.Utility_DataStructure import Test_LinkedList

l1 = Test_LinkedList()  # reference of Test_LinkedList class


class Prime_2D_Array:
    try:

        l1.prime_2d_array()  # calling function
    except RuntimeError:     # handling exception
        print("oops something went wrong...\n")
