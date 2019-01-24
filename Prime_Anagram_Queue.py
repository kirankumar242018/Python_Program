# ******************************************************************#
#  Purpose: Printing Prime Anagram Using Queue DS
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */


from DataStructure_Utility.Utility_Stack import Test_Stack
from Utility.UtilityTest import TestFunctional

q1 = Test_Stack()   # reference of a Test_Stack class


class Prime_Anagram_Queue:
    try:
        print("enter the number range to check anagram prime...\n ")
        num = int(input())              # taking user input
        prime_list = TestFunctional.prime_number(num)  # storing result of prime numbers
        anagram_list = TestFunctional.anagram_prime(prime_list)  # storing result of anagram_prime numbers

        print("Pushing elements to the Queue.....\n")
        for i in anagram_list:    # pushing elements of anagram_list into a queue
            q1.en_Queue(i)
        print()
        print("Displaying the Queue elements.....\n ")
        q1.queue_display()      # printing queue elements
    except ValueError:          # exception handling
        print("oops something went wrong.....\n")