# ******************************************************************#
#  Purpose: 12.Solving Anagram Algorithm Problem and displaying using 2D array
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */


from DataStructure_Utility.Utility_DataStructure import Test_LinkedList

l1 = Test_LinkedList()


class Anagram_Prime_2D_Array:
    try:                                # handling exception
        l1 .anagram_prime_2D_array()    # calling a method anagram _prime _2D
    except RuntimeError:                # handling exception
        print("oops something went wrong..\n")