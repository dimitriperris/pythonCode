month = int(input('Enter the month in numeric form: '))
day = int(input('Enter the day: '))
year = int(input('Enter a two-digit year: '))

if month * day == year:
    print('The date is magic!')
else:
    print('The date is not magic.')
    
