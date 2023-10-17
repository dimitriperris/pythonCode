# File: driver_license.py
# Description: Design  a program that displays the total number of correctly answered questions, the total number 
# of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions from a set of answers. 
# Assignment Name and Number: Driver's License Exam #7
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
              'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

def main():
    student_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                      'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    
    with open('student_answers.txt', 'w') as outfile:
        outfile.write(' '.join(student_answers))

    print()
    
    with open('student_answers.txt', 'r') as infile:
        perscribed_answers = infile.read().split()

    if perscribed_answers == student_answers:
        print('These are the student answers: ', perscribed_answers)
        print('You recieved a 20/20. Congrats, you passed.')
    else:
        print('These are the student answers: ', perscribed_answers)
        print('You had too many incorrect answers.')

main()


