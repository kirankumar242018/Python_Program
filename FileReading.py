import re

from Utility import UtilityTest

r1 = UtilityTest.TestFunctional


class FileReading:
    try:
        newfile = open("hello.txt", "r")
        readfile = newfile.read()
        regex = re.sub('[^A-Za-z]+', ' ', readfile)
        my_list = []
        my_list = regex.lower().split()
        print("before sorting \n")
        print(my_list)
        res = r1.insertion_sort(my_list)
        print("after aorting\n")
        print(res)
        print("enter word to search \n")
        word = input()
        if word in res:
              print("word=>", word, "found at position=>", r1.binary_search(my_list, word))
        else:
            print("element not found \n")

    except IOError:
        print("oops something went wrong\n")