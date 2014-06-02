#!/usr/bin/env python3.2

import random


class Pig:
    def __init__(self, *players):
        self.players = players

    def get_players(self):
        '''Returns a tuple of all players'''
        return self.players

    def roll(self):
        '''Returns a number between 1 and 6'''
        return random.randint(1, 6)
