# File: functions.py
# Description: Defining functions with and without parameters
# Assignment Number: N/A
#
# Name: Dimitri Perris
#
# GitHub: <YOUR GitHub>


# def starts a function definition
# names of functions follow variable naming conventions
# functions can take zero or more parameters
def is_a_party(apples, pizzas):
 
    if apples > 10 and pizzas > 10:
        return True
    else:
        return False


# A function with zero parameters

def throw_party():
    num_apples = int(input("How many apples do you have? "))
    num_pizzas = int(input("How many pizzas do you have? "))

    # Ask if this is enough for a party
    if is_a_party(num_apples, num_pizzas):
        return "Dude let's party down"
    else:
        return "You'll have to go to the store first."

## Testing the functions
print (is_a_party(20, 20))
print (is_a_party(5, 15))
print (is_a_party(5, 2))
print (is_a_party(14, 8))

print(throw_party())