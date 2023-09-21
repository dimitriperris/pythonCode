user_input = int(input("Enter a number within the range of 1 through 10: "))
if 1 <= user_input <= 10:
        if user_input == 1:
            print("The Roman numeral for 1 is I")
        elif user_input == 2:
            print("The Roman numeral for 2 is II")
        elif user_input == 3:
            print("The Roman numeral for 3 is III")
        elif user_input == 4:
            print("The Roman numeral for 4 is IV")
        elif user_input == 5:
            print("The Roman numeral for 5 is V")
        elif user_input == 6:
            print("The Roman numeral for 6 is VI")
        elif user_input == 7:
            print("The Roman numeral for 7 is VII")
        elif user_input == 8:
            print("The Roman numeral for 8 is VIII")
        elif user_input == 9:
            print("The Roman numeral for 9 is IX")
        elif user_input == 10:
            print("The Roman numeral for 10 is X")
        else:
            print("Error: Number is outside the range of 1 through 10")
else:
     print("Error: Invalid input. Please enter a valid number.")
