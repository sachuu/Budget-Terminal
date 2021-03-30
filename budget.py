import SpendObject

income = 0
keyword = ''
totalBalance = 0
monthlySpend = []
lifetimeSpend = []

while True:
    #SETUP
    if 0 >= income:
        income = int(input("What is your monthly income? "))
        print("Got it, thank you! \n")
        expenses = int(input("Any expenses so far? You can put 0 as well"))
        print("Got  \n")
        totalBalance = income - expenses
    #PARSING FOR KEYWORDS
    else:
        print("Your balance is: ${} \n".format(totalBalance))
        while(keyword != 'exit'):
            keyword = input("Let me know if you need anything or type help to see all commands ")
            if(keyword == 'add'):
                newExpense = int(input("How much was spent?"))
                expenseName = input("What did you spend it on?")
                totalBalance = totalBalance - newExpense
                print("Your new balance is ${}".format(totalBalance))
            else:
                print("Sorry I'm not sure what you mean?")
        print("Thank you for using BudgetPal")
