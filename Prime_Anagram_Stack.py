# ******************************************************************#
#  Purpose: Printing Prime Anagram Using Stack DS
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */





from DataStructure_Utility.Utility_Stack import Test_Stack
from Utility.UtilityTest import TestFunctional

t1 = Test_Stack()  # reference of a Test_Stack


class Prime_Anagram_Stack:
    try:
        print("enter range of a number to find prime numbers....\n")
        number = int(input())  # taking user inputs
        while number <= 2:  # validating user inputs
            print("enter positive and greater than 2...\n ")
            number = int(input())
        prime_list = TestFunctional.prime_number(number)  # prime number() returns the list
        anagram_list = TestFunctional.anagram_prime(prime_list) # anagram_prime returns the list

        for i in anagram_list:
            t1.stack_push(int(i))  # pushing the elements from list to stack
        print()

        print("stack values are as follows: \n")
        t1.stack_dispaly()      # printing stack elements
        print()

    except ValueError:  # handling the exceptions
        print("oops something went wrong........")