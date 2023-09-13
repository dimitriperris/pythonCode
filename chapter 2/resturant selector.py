print()
vegatarian= input('Is there anyone in your party that is vegatarian? :')
print()
vegan= input('Is there anyone in your party that is vegan? :')
print()
glutenf= input('Is there anyone in your party that is gluten free? :')

if vegatarian == 'yes' or vegatarian == 'no':
    if vegatarian == 'yes':
        if vegan == 'yes':
            if glutenf == 'yes':
                print('You along with your friends can go to the Chefs Kitchen or the Corner Cafe.')
            else: 
                if glutenf == 'yes':
                    print('You along with your friends can go to the Main Street Pizza Company.')
        else:
            if vegan == 'no' and vegatarian == 'yes':
                print('You along with your friends can go to Mamas Fine Italian.')
            else: 
                if vegatarian == 'no' and vegan == 'no' and glutenf == 'no': 
                    print('You along with your friends can go to Joes Gourmet Burgers')
    else:
        print('Error, enter either yes or no to proceed.')
        print()



