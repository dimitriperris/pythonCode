# File: falling_distance.py
# Description: Write a function that accepts an object's falling time in seconds. 
# Assignment Name and Number: Falling Distance #13
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

def falling_distance(time):
    gravity = 9.8  
    distance = 0.5 * gravity * (time ** 2)
    return distance

def main():
    time = float(input('Enter the time in seconds: '))
    
    distance = falling_distance(time)
    
    print('The object has fallen', distance, 'meters in', time, 'seconds.')

main()
