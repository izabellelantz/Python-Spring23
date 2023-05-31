"""
Program: keyword_and_arg.py
Name: Izabelle Lantz
Date: 03/20/2023
The purpose of this program is to take arbitrary arguments and find the GPA and
also take keyword arguments and then display them to the user in the form of a string once
run.
"""
def average_scores(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    avg = total / len(args)
    gpa_disp = f'gpa={str(avg)}'
    for key, value in kwargs.items():
        print("%s==%s" % (key, value))
    print(gpa_disp)


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, student_name='Steven', course='Python'))
