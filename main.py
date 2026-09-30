import datetime
import matplotlib.pyplot as plt
import pandas as pd


def addExpense(category:str, amount:int):
    new_expense = {'Date': [str(datetime.datetime.now().date())], 'Category': [category], 'Amount': [amount]}
    df_new = pd.DataFrame(new_expense)
    df_new.to_csv('data.csv', mode='a', index=False, header=False)



balance = 0

print("*************Budget Buddy***************")
print("Add Income (i)")
print("Add expense (e)")
print("Show Balance (b)")
print("Transaction History (t)")
print("Report (r)")
print("Exit (q)")

while True:
    cmd = input("Enter Command: ")

    if cmd == "i":
        print("************************")
        print("*", end=" ")
        amt = int(input("Enter amount: "))
        balance += amt
        print("*", end=" ")
        print(f"{amt} added to your balance!")
        print("************************")

    elif cmd == "e":
        print("************************")
        print("*", end=" ")
        cat = input("Category: ")
        print("*", end=" ")
        amt = int(input("Enter amount: "))
        addExpense(cat, amt)
        balance -= amt
        print("*", end=" ")
        print(f"Expense of {amt} made for {cat}")
        print("************************")

    elif cmd == "b":
        print("************************")
        print("*", end=" ")
        print(f"Your curret balance: {balance}")
        print("************************")
    elif cmd == "t":
        print("************************")
        df = pd.read_csv('data.csv')
        print(df)
        print("************************")
    elif cmd == "r":
        df = pd.read_csv('data.csv')
        if df.empty:
            print("************************")
            print("*", end=" ")
            print("No expenses recorded yet!")
            print("************************")
        else:
            dates = pd.to_datetime(df['Date'], format='mixed')
            days = dates.dt.day.astype(str)
            month = dates.dt.strftime('%B').iloc[-1]
            plt.bar(days, df['Amount'])
            plt.xlabel(f"Date ({month})")
            plt.ylabel("Expense Amount")
            plt.title("Expense vs Dates")
            plt.show()
    elif cmd == "q":
        break
    else:
        print("************************")
        print("*", end=" ")
        print("Not a valid command\nUse these:\n")
        print("Add Income (i)")
        print("Add expense (e)")
        print("Show Balance (b)")
        print("Transaction History (t)")
        print("Report (r)")
        print("Exit (q)")
        print("************************")
















