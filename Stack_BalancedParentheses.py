# ******************************************************************#
#  Purpose: Printing Balanced Parentheses Using Stack
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */


from DataStructure_Utility.Utility_DataStructure import Test_LinkedList

l1 = Test_LinkedList()  # reference of Test_LinkedList class


class Stack_BalancedParentheses:
    try:
        print("enter expression:\n")
        values = input()    # taking user input
        size = len(values)  # length of input
        list1 = []          # taking list
        list2 = []          # taking list
        for i in range(len(values)):
            if values[i] == '(' or values[i] == '{' or values[i] == '[':
                list1 = l1.push(values[i])      # if input contains (,{,[ push into the stack,and storing into the list1
            elif values[i] == ')' or values[i] == '}' or values[i] == ']':
                l1.pop()                        # if input contains  ),],} pop corresponding (,{,[ elements from a stack
            else:
                list2 = l1.push(values[i])                          # other than parentheses store it in a list2

        print()
        print("elements of stack elements...\n")
        for i in list1:
            print(i, end="=> ")                                     # printing the stack elements
        """print("checking stack is empty or not...\n")
        l1.st_isEmpty()
        print("checking stack size...\n")
        l1.st_size()"""
        print()
        print("===============================================")
        if '(' not in list1 and '{' not in list1 and '[' not in list1:  # validating for balanced parentheses
            print("balanced parentheses....\n")
        else:
            print("unbalanced parentheses....\n")
    except RuntimeError:                                                 # exception handling
        print("oops something went wrong....\n")
