# Kynaesha Rodriguez
# P5LAB Assignment
# This program simulates a self-checkout machine that shows how much change a customer will receive.
# It uses random numbers and a function to break the change into dollars and coins.

import random
def disperse_change(change_amount):
    cents = int(round(change_amount * 100))

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    if dollars > 0:
        print(f"{dollars} Dollar" if dollars == 1 else f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarter" if quarters == 1 else f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dime" if dimes == 1 else f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickel" if nickels == 1 else f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Penny" if pennies == 1 else f"{pennies} Pennies")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    cash_given = float(input("How much cash will you put in the self-checkout? "))
    change = round(cash_given - total_owed, 2)
    if change < 0:
        print("Not enough money given.")
    elif change == 0:
        print("No change needed.")
    else:
        print(f"Change is: ${change:.2f}")
        disperse_change(change)
if __name__ == "__main__":
    main()