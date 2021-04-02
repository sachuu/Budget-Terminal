income = 0
keyword = ''

totalBalance = 0

monthlySpend = []
lifetimeSpend = []

# Used as a reference to create a new instance of a
# spend object
currItem = 0


class SpendItem:
    def __init__(self, nickname, price):
        self.nickname = nickname
        self.price = price


def printspend():
    for i in lifetimeSpend:
        print("Name: " + "  " + "Cost: ")
        print("{}    {}".format(i.nickname, i.price))


while True:
    # SETUP
    # Process goes get income then update automatically the next month
    if 0 >= income:
        income = int(input("What is your monthly income? "))
        print("Got it, thank you! \n")
        expenses = int(input("Any expenses so far? You can put 0 as well "))
        print("Got  \n")
        totalBalance = income - expenses
        print("You're all set up")
    # PARSING FOR KEYWORDS
    else:
        print("Your balance is: ${} \n".format(totalBalance))
        while keyword != 'exit':
            keyword = input("Let me know if you need anything or type help to see all commands ")
            if keyword == 'add':
                newExpense = int(input("How much was spent?"))
                expenseName = input("What did you spend it on?")
                currItem = currItem + 1
                instance = SpendItem(expenseName, newExpense)
                lifetimeSpend.append(instance)
                totalBalance = totalBalance - newExpense
                print("Your new balance is ${} \n".format(totalBalance))
                printspend()
            elif keyword == 'help':
                print()
            else:
                print("Sorry I'm not sure what you mean?")
        print("Thank you for using BudgetPal")


