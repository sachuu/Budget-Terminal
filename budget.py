income = 0

while True:
    if 0 >= income:
        income = int(input("What is your monthly income?"))
        print("Ok Thank You")
        expenses = int(input("Any expenses so far? You can put 0 as well"))
        print("Got it")
    else:
        spent = int(input("Spent any money?"))
        print("New total is")
        income = income - spent
        print(income)
