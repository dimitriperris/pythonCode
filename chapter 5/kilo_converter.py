def kilo_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

def main():
    try:
        kilometers = float(input('Enter a distance in kilometers: '))
        miles = kilo_miles(kilometers)
        print('Kilometers', kilometers, 'is equal to miles', miles)
    except ValueError:
        print('Error. Please enter a correct number for kilometers.')

main()
