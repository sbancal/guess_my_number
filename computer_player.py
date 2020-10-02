#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020-10-02

@author: Samuel Bancal

This script will try to guess the mysterious number
prepared by guess_my_number.GuessMachine.

It's strategy is to try random numbers between min and max.
It'll adapt min and max values to match GuessMachine answers.
"""

import random

from guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
    min = MIN
    max = MAX
    guess_nachine = GuessMachine()
    while True:
        attempt = random.randint(min, max)
        result = guess_nachine.guess(attempt)
        print('tried %d : %s' % (attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' % guess_nachine.number_of_attempt)
            break
        elif result == 'too low':
            min = attempt + 1
        else:
            max = attempt - 1
