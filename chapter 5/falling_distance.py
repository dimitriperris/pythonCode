def falling_distance(time):
    gravity = 9.8  
    distance = 0.5 * gravity * (time ** 2)
    return distance

def main():
    time = float(input('Enter the time in seconds: '))
    
    distance = falling_distance(time)
    
    print('The object has fallen', distance, 'meters in', time, 'seconds.')

main()
