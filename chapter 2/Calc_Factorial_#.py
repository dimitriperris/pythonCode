number = int(input("Enter a positive integer:"))
factorial = 1

if number >= 0:
    for i in range(1, number + 1):
        factorial *= i
    print('=',factorial)
else:
    print("Please enter a nonnegative integer.")
