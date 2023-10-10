numbers = []

for n in range(20):
    try:
        number = float(input(f'Enter number {n + 1}: '))
        numbers.append(number)
    except ValueError:
        print('Invalid input. Please enter a valid number.')

if numbers:
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print('Lowest number:', lowest)
    print('Highest number:', highest)
    print('Total of the numbers:', total)
    print('Average of the numbers:', average)


