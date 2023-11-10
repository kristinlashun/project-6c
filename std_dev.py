# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: November 9th 2023
# Description: Program to calculate standard deviation of ages of Person objects.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

def std_dev(person_list):
    n = len(person_list)
    if n == 0:
        return None

    mean_age = sum(person.age for person in person_list) / n
    variance = sum((person.age - mean_age) ** 2 for person in person_list) / n
    return variance ** 0.5

