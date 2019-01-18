# ****************************** Prime_Anagram_Palandrome  Problem  ************************************#
#  Purpose: Solving Prime_Anagram_Palandrom  Algorithm
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
#

from Utility import UtilityTest

p1 = UtilityTest.TestFunctional


class Prime_Anagram:
    try:
        my_list = []
        my_list1 = []
        n = int(input("enter a range....\n"))

        my_list = p1.prime_number(n)
        my_list1 = p1.anagram_prime(my_list)

        print("List Of All Palindrome Numbers :")
        for i in range(len(my_list)):
            res = p1.palindrome(int(my_list[i]))
            if res is not None:
                print(res)
    except RuntimeError:
        print("oops something went wrong....")
