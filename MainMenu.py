# preparing a menu for HAB Taxi services
# Main menu created by Kyle Snow
# Option 1 created Devin Augot
# Option 6 created by Kyle Snow
# Option 7 created by Jacob Thomas
# Completion date: 2022-08-15


import Option1
import Option6
import Option7


# Main menu program

while True:
    print()
    print("    HAB Taxi Services    ")
    print("    Company Services System                    ")
    print()
    print(" 1. Enter a New Employee (driver). ")
    print(" 2. Enter Company Revenues. ")
    print(" 3. Enter Company Expenses. ")
    print(" 4. Track Car Rentals.")
    print(" 5. Record Employee Payment. ")
    print(" 6. Print Company Profit Listing.")
    print(" 7. Print Driver Financial Listing.")
    print(" 8. Quit Program.")
    print()

# Gathering and validating the users inputted option.

    while True:
        try:
            Selection = input(" Enter choice (1-8): ")
            Selection = int(Selection)
        except:
            print(" Error - Invalid Input")
        else:
            if Selection < 1 or Selection > 8:
                print(" Error - Must be 1 to 8 ")
            else:
                break

    print()

# Determining output based on the users input

    if Selection == 1:
        Option1.OptionOne()
    if Selection == 2:
        while True:
            print("Sorry this option isn't available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 3:
        while True:
            print("Sorry this option isn't available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 4:
        while True:
            print("Sorry this option isn't available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 5:
        while True:
            print("Sorry this option isn't available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 6:
        Option6.OptionSix()
    if Selection == 7:
        Option7.option7()
    if Selection == 8:
        print("Thanks for using this program.")
        break
