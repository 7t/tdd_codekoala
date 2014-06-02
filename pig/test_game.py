#!/usr/bin/env python3.2

from unittest import TestCase
import game


class GameTest(TestCase):
    def test_join(self):
        '''Players may join a game of Pig'''
        pig = game.Pig('PlayerA', 'PlayerB', 'PlayerC')
        self.assertTupleEqual(pig.get_players(),
                              ('PlayerA', 'PlayerB', 'PlayerC'))
