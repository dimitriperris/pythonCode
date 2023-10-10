import random

responses = ['Yes', 'No', 'Maybe', 'Ask again later', 'Im not sure', 'Absolutely', 'Dont count on it', 'It is certain', 'Very doubtful', 'Without a doubt', 'Outlook not so good', 'Reply hazy, try again']

while True:
    input('Ask a yes or no question: ')
    print('Magic 8 Ball says', random.choice(responses))
    
    play_again = input('Do you want to ask another question? (yes or no): ')
    if play_again.lower() != 'yes':
        break
