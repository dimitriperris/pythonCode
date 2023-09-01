# The amount of principal originally deposited into the account
# The annual interest rate paid by the account
# The number of times per year that the interest is compounded (For example, if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.)
# The number of years the account will be left to earn interest

principal= float(input('Enter the principal amount that was originally deposited into the account: '))
interest_rate= float(input('Enter the annual interest paid by the account as a decimal: '))
interest_compounded= float(input('Enter the number of times per year that the interest is compounded: '))
years= float(input('Enter the number of years the account will be left to earn interest: '))

# Amount of money 
interest_rate = (principal * ((1 + (interest_rate / interest_compounded)) ** (interest_compounded * years)))

print('The amount of money that will be in the account after', years, 'years is,', interest_rate, '$')
