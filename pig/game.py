#!/usr/bin/env python3.2


class Pig:
    def __init__(self, *players):
        self.players = players

    def get_players(self):
        '''Returns a tuple of all players'''
        return self.players
