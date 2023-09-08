
def number_to_roman(num):
    if num == 1:
        return "I"
    elif num == 2:
        return "II"
    elif num == 3:
        return "III"
    elif num == 4:
        return "IV"
    elif num == 5:
        return "V"
    elif num == 6:
        return "VI"
    elif num == 7:
        return "VII"
    elif num == 8:
        return "VIII"
    elif num == 9:
        return "IX"
    elif num == 10:
        return "X"
    else:
        return ()


try:
    user_input = int(input("Enter a number between 1 and 10: "))
    
    
    if 1 <= user_input <= 10:
        roman_numeral = number_to_roman(user_input)
        print(f"The Roman numeral for {user_input} is {roman_numeral}.")
    else:
        print("Error: Please enter a number within the range of 1 through 10.")
except ValueError:
    print("Error: Invalid input, please enter a valid number.")
