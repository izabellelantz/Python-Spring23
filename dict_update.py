"""
Program: dict_update.py
Name: Izabelle Lantz
Date: 03/22/2023
This program takes valid test scores and puts them into a dictionary in one function,
then uses another to find the average and displays both to user.
"""
def get_test_scores():
    scores_dict = dict()
    num_scores = input('How many scores will you be entering?')
    i = 0
    key = 1
    while i < int(num_scores):
        score = input('Input test score: ')
        try:
            score = int(score)
        except ValueError:
            raise ValueError('invalid input')
        if 0 < score <= 100:
            scores_dict.update({f'Test {key}': score})
            key += 1
            i += 1
    return scores_dict
    

def average_scores(scores_dict):
    num_scores = len(scores_dict)
    i = 0
    total = 0
    while i < num_scores:
        for value in scores_dict.values():
            total += value
            i += 1
    avg = total / num_scores
    return avg


if __name__ == '__main__':
    my_dict = ({'1': 3, '2': 43, '3': 67, '4': 55})
    print(average_scores(my_dict))
    
    score_dict1 = get_test_scores()
    print(average_scores(score_dict1))
