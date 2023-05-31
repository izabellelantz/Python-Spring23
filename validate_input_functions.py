"""
Name: Izabelle Lantz
Date: 02/22/2023
Program: validate_input_functions.py
The purpose of this program is to take a test name and score and validate
the test score using a function then display the test name and score to the user if
the score is valid.
"""


def score_input(test_name, test_score, invalid_message='Invalid test score!'):
    try:
        test_score = int(test_score)
    except ValueError:
        print('ValueError raised!')
        raise
    if 0 <= test_score <= 100:
        return str(test_name) + ' ' + str(test_score)
    if test_score < 0 or test_score > 100:
        return invalid_message
    

if __name__ == '__main__':
    display_string = score_input('Test 1', 80)
    print(display_string)
 
    print(score_input('Test 2', -1))
 
    print(score_input('Test 3', 101))
 
    print(score_input('Test 4', 'j'))
