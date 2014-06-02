#!/usr/bin/env python3.2

from unittest import TestCase
import mock
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

    def test_get_player_names(self):
        '''Players can enter their names'''
        fake_input = mock.Mock(side_effect=['A', 'M', 'Z', ''])
        with mock.patch('builtins.input', fake_input):
            names = game.get_player_names()
        self.assertEqual(names, ['A', 'M', 'Z'])

    def test_get_player_names_stdout(self):
        '''Check the prompts for player names'''
        with mock.patch('builtins.input', side_effect=['A', 'B', '']) as fake:
            game.get_player_names()
        fake.assert_has_calls([
            mock.call("Player 1's name: "),
            mock.call("Player 2's name: "),
            mock.call("Player 3's name: "),
        ])
