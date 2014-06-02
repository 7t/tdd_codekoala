#!/usr/bin/env python3.2

from unittest import TestCase
import game


class GameTest(TestCase):
    def setUp(self):
        self.pig = game.Pig('PlayerA', 'PlayerB', 'PlayerC')

    def test_join(self):
        '''Players may join a game of Pig'''
        self.assertTupleEqual(self.pig.get_players(),
                              ('PlayerA', 'PlayerB', 'PlayerC'))

    def test_roll(self):
        for i in range(500):
            res = self.pig.roll()
            self.assertIsInstance(res, int)
            self.assertTrue(1 <= res <= 6)
