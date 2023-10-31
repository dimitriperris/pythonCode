import random

us_states_and_capitals = {'Alabama': 'Montgomery','Alaska': 'Juneau',
    'Arizona': 'Phoenix','Arkansas': 'Little Rock',
    'California': 'Sacramento','Colorado': 'Denver', 'Connecticut': 'Hartford',
    'Delaware': 'Dover','Florida': 'Tallahassee','Georgia': 'Atlanta','Hawaii': 'Honolulu',
    'Idaho': 'Boise','Illinois': 'Springfield','Indiana': 'Indianapolis',
    'Iowa': 'Des Moines','Kansas': 'Topeka','Kentucky': 'Frankfort','Louisiana': 'Baton Rouge',
    'Maine': 'Augusta','Maryland': 'Annapolis','Massachusetts': 'Boston','Michigan': 'Lansing',
    'Minnesota': 'St. Paul','Mississippi': 'Jackson','Missouri': 'Jefferson City',
    'Montana': 'Helena','Nebraska': 'Lincoln','Nevada': 'Carson City','New Hampshire': 'Concord',
    'New Jersey': 'Trenton','New Mexico': 'Santa Fe','New York': 'Albany','North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck','Ohio': 'Columbus','Oklahoma': 'Oklahoma City','Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg','Rhode Island': 'Providence','South Carolina': 'Columbia',
    'South Dakota': 'Pierre','Tennessee': 'Nashville','Texas': 'Austin','Utah': 'Salt Lake City',
    'Vermont': 'Montpelier','Virginia': 'Richmond','Washington': 'Olympia',
    'West Virginia': 'Charleston','Wisconsin': 'Madison','Wyoming': 'Cheyenne'}

def main():
    correct_answers = 0
    incorrect_answers = 0

    print('THE STATE CAPITAL QUIZ!!')

    while len(us_states_and_capitals) > 0:
        state, capital = us_states_and_capitals.popitem() 
        guess = input(f"What's the capital of {state}? ").strip()

        if guess == capital:
            print('Correct!')
            correct_answers += 1
        else:
            print('Incorrect, the capital of', state, 'is', capital)
            incorrect_answers += 1

    print("That's all 50. Congrats, you finished!")
    print('You got', correct_answers, 'questions correct and', incorrect_answers, 'questions wrong.')

main()
