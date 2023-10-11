# File: stadium_seat.py
# Description: Write a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.
# Assignment Name and Number: Stadium Seating #7
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    class_A_tickets = int(input('Enter the number of Class A tickets sold: '))
    class_B_tickets = int(input('Enter the number of Class B tickets sold: '))
    class_C_tickets = int(input('Enter the number of Class C tickets sold: '))

    class_A_price = 20
    class_B_price = 15
    class_C_price = 10

    income_A= class_A_tickets * class_A_price
    income_B = class_B_tickets * class_B_price
    income_C = class_C_tickets * class_C_price

    total_income = income_A + income_B + income_C

    print('Class A tickets sold', class_A_tickets)
    print('Class B tickets sold', class_B_tickets)
    print('Class C tickets sold', class_C_tickets)
    print('Total income generated $', total_income)

main()
