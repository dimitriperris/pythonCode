number_of_days= int(input('Enter the number of days worked.:'))
salary= 0.005 

for day in range(1, number_of_days + 1):
    salary *= 2.0
    print('Day', day, 'salary', salary)
print('Your salary on day', number_of_days, 'would be', salary)
          

