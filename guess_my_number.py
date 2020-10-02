#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:13:09 2020

@author: Samuel Bancal

This offers a Class to play at "Guess my number".

It can also be run as is ... which will play interactively
with the user and let him look for the mystery number.
"""

import random

MIN = 0
MAX = 1000


class GuessMachine():
    '''
    I have a number in mind,
    you have to guess it!!

    + self._number_to_guess is generated durinig creation of the object
    + Use `guess(num)` method to make a guess
    + I'll count the number ot attempt in self.number_of_attempt
    '''

    def __init__(self):

        self._number_to_guess = random.randint(MIN, MAX)
        self.number_of_attempt = 0

    def guess(self, num):
        '''
        Attempt to find the right number
        it returns 'too high', 'too low', 'found'
        '''
        self.number_of_attempt += 1
        if num < self._number_to_guess:
            return 'too low'
        elif num > self._number_to_guess:
            return 'too high'
        else:
            return 'found'


if __name__ == '__main__':
    guess_nachine = GuessMachine()
    print('Hey! Try to guess a number between %d and %d!' % (MIN, MAX))

    while True:
        user_input = input('Your guess? ')
        try:
            user_attempt = int(user_input)
            result = guess_nachine.guess(user_attempt)
            if result == 'found':
                print(
                    'Fantastic, you coud find '
                    'the number I had in mind '
                    'in %d attempts!' % guess_nachine.number_of_attempt)
                break
            else:
                print(result)
        except ValueError:
            print('You joker ... that was not an integer!')
