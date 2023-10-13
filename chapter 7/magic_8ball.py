# File: magic_8ball.py
# Description: Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a random response to a yes or no question. 
# Assignment Name and Number: Magic 8 Ball #13
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

responses = ['Yes, of course', 'No way!', 'For sure!', 'Ask me later', 'Im not sure', 'I cant tell you right now', 'Ill tell you after my nap', 'No way!', 'I dont think so', 'Without a doubt, yes', 'Without a doubt, no', 'The answer is clearly NO']

while True:
    input('Ask a yes or no question: ')
    print('Magic 8 Ball says', random.choice(responses))
    
    play_again = input('Do you want to ask another question? (yes or no): ')
    if play_again.lower() != 'yes':
        break
