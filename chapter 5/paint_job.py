def main():
    sqr_ft = float(input('Enter the square feet of wall space to be painted: '))
    paint_price = float(input('Enter the price of paint per gallon: '))

    gallons_required = sqr_ft / 112
    hours_required = gallons_required * 8
    paint_cost = gallons_required * paint_price
    labor_charges = hours_required * 35
    total_cost = paint_cost + labor_charges

    print('Gallons of paint required', gallons_required)
    print('Hours of labor required', hours_required)
    print('Cost of the paint', paint_cost)
    print('Labor charges', labor_charges)
    print('Total cost of the paint job', total_cost)

main()
