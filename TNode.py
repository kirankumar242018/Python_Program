# ******************************************************************#
#  Purpose: Implementing Node Class For Stack
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */

""""======creating node class for Stack====="""


class TNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNext(self):
        return self.next

    def setNext(self, val):
        self.next = val
