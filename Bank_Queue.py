# ******************************************************************#
#  Purpose: Solving Banking Queue Using Queue Data structure
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   21-01-2019
#
# */


from DataStructure_Utility.Utility_DataStructure import Test_LinkedList

l1 = Test_LinkedList()


class Bank_Queue:
    cash = []
    try:

        print("enter the amount minimum 500 to open account...\n")
        amount = int(input())                 # initial amount
        while amount < 500:                   # validating the input
            print("please enter above 500 to open account...")
            amount = int(input())             # accepting valid input
        print("enter number of peoples in queue..\n")
        customer = int(input())               # number of people in queue
        temp = amount                         # assigning inputs into temp,temp1 variables
        temp1 = customer
        while customer > 0:                   # customers greater than 0 process further
            print("WELCOME TO YOUR BANK.... \n")

            print("1.Deposit \n 2.Withdraw...\n 3.process 4.exit..\n")
            print("enter your choice..\n")

            choice = int(input())              # taking customers inputs
            while choice > 4:                  # validating the inputs
                print("please enter choice within range 4...\n")
                choice = int(input())

            if choice == 1:     # if choice is 1 deposit the money
                print("enter amount to deposit...\n")
                deposit = int(input())     # input amount
                while deposit < 100:       # validating
                    print("enter above 100 rupees..\n")
                    deposit = int(input())
                amount = amount + deposit     # add deposit amount to the initial amount
                cash = l1.queue_push(deposit)  # push into queue
                customer -= 1                  # decrement customer size

            if choice == 2:   # if choice is 2  withdrawing amount form bank
                print("enter amount to be withdraw from bank...")
                withdraw = int(input())
                while withdraw <= 0:   # validating
                    print("enter amount in positive numbers...\n")
                    withdraw = int(input())
                if withdraw < amount:    # withdraw amount is less than initial amount then withdraw from a bank
                    amount = amount - withdraw
                    cash = l1.queue_push(withdraw)   # push withdraw amount into a queue
                    customer -= 1                   # decrement customer size by 1
                else:                               # else print
                    print("insufficient balance please give below bank_balance...\n")

            if choice == 3: # choice 3 to process the queue
                if len(cash) != 0:  # len of cash not equal to 0
                    if customer > 0: # customer size should greater than 0
                        print("your transaction is complete..:", cash[0]) # printing the cash
                        l1.queue_pop()    # then pop
                        customer += 1     # increment by 1
                else:
                    print("no transaction to process....\n")  # else print
            if choice == 4:  # choice 4 to exit
                break
        if len(cash) != 0:
            print("Queue is full,process it..\n ")
            for i in range(temp1):
                print("process is complete.. ", cash[0])
                l1.queue_pop()
            print()

        if amount >= temp:  # to balance the cash must satisfy if condition
            print("cash is balance...\n")
        else:
            print("cash is not balanced...\n")
    except ValueError:  # handling exception
        print("please enter valid input.....")
