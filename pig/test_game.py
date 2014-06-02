#!/usr/bin/env python3.2

from unittest import TestCase
import game


class GameTest(TestCase):
    def setUp(self):
        self.pig = game.Pig('PlayerA', 'PlayerB', 'PlayerC')

    def test_get_players(self):
        '''Players may join a game of Pig'''
        self.assertTupleEqual(self.pig.get_players(),
                              ('PlayerA', 'PlayerB', 'PlayerC'))

    def test_roll(self):
        '''A roll of the die results in an integer between 1 and 6'''
        for i in range(500):
            res = self.pig.roll()
            self.assertIsInstance(res, int)
            self.assertTrue(1 <= res <= 6)

    def test_get_scores(self):
        '''Player scores can be retrieved'''
        self.assertDictEqual(self.pig.get_scores(),
                             {'PlayerA': 0, 'PlayerB': 0, 'PlayerC': 0})
