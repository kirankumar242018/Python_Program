# ****************************** Utility Functions ************************************#
#  Purpose: Solving Data Structure Problem Using Stack and Queue
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   23-01-2019
#
# */

"""======Utility data structure solving using stack and queue======"""

from DataStructure.TNode import TNode


class Test_Stack:
    head = None
    size = 0
    top = -1

    def __init__(self):
        """
        Constructor of this class
        """
        self.top = None
        self.size = 0
        self.head = None
        self.front = None
        self.rear = None
        pass

    """=====stack functions==========="""

    def stack_push(self, data):     # instance method accepts data as input
        node = TNode(data)          # assigning Node(data) into the node
        self.size += 1              # increment size by 1
        if self.top is None:        # where stack is empty add data to the first node itself
            self.top = node
        else:                       # adding data to the stack
            node.next = self.top    # else store data into a next node
            self.top = node
        print(node.data, end=" ")   # printing the node data

    def stack_pop(self):            # instance method accepts none
        if self.top is None:        # if top is None,stack is empty
            print("stack is empty...")
        # while self.top is not None:
        temp = self.top             # using temp traverse to next node
        self.top = self.top.next    # traverse from head to next node
        self.size -= 1              # decrement size by 1
        # print(temp.data, end=" ")
        return temp.data            # return temp.data

    def stack_dispaly(self):        # instance method accepts none
        my_list = []
        temp = self.top             # temp pointing to the first node
        while temp is not None:     # loop up to temp is None
            # print("reverse order...\n")
            print(temp.data, "=>", end=" ")     # printing temp data
            my_list.append(temp.data)           # append temp.data into a my_list
            temp = temp.next                    # traverse to next node
        return my_list                          # return my_list

    def stack_getSize(self):                    # instance method accepts none
        return self.size                        # return size

    """========================queue functions==============="""

    def en_Queue(self, data):                   # instance method accepts data as input
        node = TNode(data)                      # assigning Node(data) into the node
        if self.rear is None:                   # if rear is none
            self.front = node                   # assign node to front,rear
            self.rear = node
        else:
            self.rear.next = node               # traverse to rear.next
            self.rear = self.rear.next          # assign rear = rear.next
        self.size = self.size + 1               # increment size by 1
        print(node.data, end="=>")              # printing node.data

    def de_queue(self):                         # instance method accepts none

        if self.front is not None:              # check condition front is not none
            temp = self.front                   # temp holds the data of a front
            self.front = self.front.next        # jumps to next node
            # print(temp.data)
            return temp.data                    # returns the data
        else:
            if self.rear is not None:           # else rear is not none
                self.rear = None                # assign rear to none
                print("queue is empty...\n")

    def queue_display(self):                    # instance method accepts none
        temp = self.front
        while temp is not None:                 # traverse up to queue is None
            print(temp.data, end="=>")          # printing the data
            temp = temp.next                    # traverse up to last node


t = Test_Stack()

"""def stack_size(self):
       size = 1
       traverse = self.head
       if self.head is None:  # empty stack
           return 0
       while traverse.next is not None:
           traverse = traverse.next
           size += 1
       return size"""

"""def is_Stack_Empty(self):
    if t.stack_size() is None:  # size of a stack == 0 means no elements are present in a stack
        return True
    else:
        return False  # else return false"""

"""def display(self):
    traverse = self.head
    if self.top <= -1:
        print("stack is under flow...\n")
        return
    if traverse is None:
        print("stack is empty....\n")
        return
    while traverse.next is not None:
        print(traverse.data)
        traverse = traverse.next
    print(traverse.data)"""  # stack display

"""def peek(self):
    traverse = self.head
    if self.head is None:
        return "stack is empty"  # empty stack...
    self.top = t.stack_size() - 1
    # print(self.top)
    for i in range(0, self.top):
        traverse = traverse.next
    return traverse.data"""

"""def balanced_parentheses(self, string):
    for i in string:
        if i == '(' or i == '[' or i == '{':
            t.push(i)
        if ((t.peek() == '(' and i == ')') or (t.peek() == '[' and i == ']') or
                (t.peek() == '{' and i == '}') and t.stack_size() > 0):
            t.pop()
            continue
    if t.stack_size() is None:
        print("balanced parentheses...\n")
    else:
        print("unbalanced parentheses...\n")"""  # stack balanced parentheses

"""def pop(self):
    traverse = self.head
    if self.head is None:  # stack is empty
        return -1
    if self.head.next is None:  # only one element in stack
        self.head = None
        return traverse.data
    while traverse.next is not None:
        temp = traverse.next
        if temp.next is None:  # delete last node which is top on the stack
            traverse.next = None
            return temp.data
        traverse = traverse.next"""  # stack pop
"""def push(self, data):
       node = TNode(data)
       if self.head is None:  # if head is empty add data to the head
           self.head = node
       else:  # else add node to the next node
           traverse = self.head
           while traverse.next is not None:
               traverse = traverse.next
           traverse.next = node"""  # stack push