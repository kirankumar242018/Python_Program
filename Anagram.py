# ******************************************************************#
#  Purpose: Solving Anagram Algorithm Problem
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */




from Utility import UtilityTest

a1 = UtilityTest.TestFunctional


class Anagram:
    try:
        str1 = str(input("enter a string1..\n"))
        str2 = str(input("enter a string2..\n"))
        a1.anagram(str1, str2)
    except RuntimeError:
        print("oops something went srong...\n")
