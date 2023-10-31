def main():
    mean_radius = {"Io": "1821.6", "Europa": "1560.8", "Ganymede": "2634.1", "Callisto": "2410.3"}
    surface_gravity = {"Io": "1.796", "Europa": "1.314", "Ganymede": "1.428", "Callisto": "1.235"}
    orbital_period = {"Io": "1.769", "Europa": "3.551", "Ganymede": "7.154", "Callisto": "16.689"}

    moon_name = input("Enter the name of a Galilean moon of Jupiter (Io, Europa, Ganymede, Callisto): ")

    if moon_name in mean_radius:
        print('Mean Radius is:', mean_radius[moon_name], 'kilometers')
    if moon_name in surface_gravity:
        print('Surface Gravity:', surface_gravity[moon_name], 'meters per second squared.')
    if   moon_name in orbital_period:
        print('Orbital Period:', orbital_period[moon_name], 'days.')
    else:
        print('Invalid, please enter the correct moon name.')

main()




    
    


