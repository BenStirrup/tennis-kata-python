import unittest

from tennis import Set, Game, DisplayScore


class Test(unittest.TestCase):
    def setUp(self):
        self.set: Set = Set("Charlotte", "Annabelle")

    def test_points_winned_must_be_positive(self):
        self.assertRaises(ValueError, self.set.add_points, -2, 1)

    def test_scores_must_have_valid_values_when_deuce_activated(self):
        self.assertRaises(ValueError, self.set.add_points, 7, 4)

    def test_scores_must_have_valid_values_when_deuce_not_activated(self):
        self.assertRaises(ValueError, self.set.add_points, 6, 2)

    def test_player1_scores_fifteen_in_one_game(self):
        self.set.add_points(1, 0)
        scores = self.set.get_current_game_display_scores()
        expected_scores = (DisplayScore.FIFTEEN, DisplayScore.ZERO)
        self.assertEqual(scores, expected_scores)

    def test_player1_and_player2_both_score_thirty_in_one_game(self):
        self.set.add_points(2, 2)
        scores = self.set.get_current_game_display_scores()
        expected_scores = (DisplayScore.THIRTY, DisplayScore.THIRTY)
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_one_game_without_deuce(self):
        self.set.add_points(4, 2)
        scores = self.set.get_previous_games_display_scores()
        expected_scores = [(DisplayScore.WIN, DisplayScore.THIRTY)]
        self.assertEqual(scores, expected_scores)

    def test_player1_has_advantage_in_one_game(self):
        self.set.add_points(4, 3)
        scores = self.set.get_current_game_display_scores()
        expected_scores = (DisplayScore.ADVANTAGE, DisplayScore.DEUCE)
        self.assertEqual(scores, expected_scores)

    def test_player1_has_advantage_and_large_score_in_one_game(self):
        self.set.add_points(10, 9)
        scores = self.set.get_current_game_display_scores()
        expected_scores = (DisplayScore.ADVANTAGE, DisplayScore.DEUCE)
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_one_game_with_deuce(self):
        self.set.add_points(5, 3)
        scores = self.set.get_previous_games_display_scores()
        expected_scores = [(DisplayScore.WIN, DisplayScore.DEUCE)]
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_one_game_with_deuce_and_large_score(self):
        self.set.add_points(10, 8)
        scores = self.set.get_previous_games_display_scores()
        expected_scores = [(DisplayScore.WIN, DisplayScore.DEUCE)]
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_one_game_and_player2_wins_two_games(self):
        self.set.add_points(8, 6)
        self.set.add_points(1, 4)
        self.set.add_points(6, 8)
        scores = self.set.get_previous_games_display_scores()
        expected_scores = [
            (DisplayScore.WIN, DisplayScore.DEUCE),
            (DisplayScore.FIFTEEN, DisplayScore.WIN),
            (DisplayScore.DEUCE, DisplayScore.WIN),
        ]
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_set_without_seventh_game(self):
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)

        winner = self.set.winner
        scores = self.set.get_previous_games_display_scores()
        expected_winner = "Charlotte"
        expected_scores = [
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
        ]
        self.assertEqual(winner, expected_winner)
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_set_with_seventh_game(self):
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(0, 4)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)

        winner = self.set.winner
        scores = self.set.get_previous_games_display_scores()
        expected_winner = "Charlotte"
        expected_scores = [
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.ZERO, DisplayScore.WIN),
            (DisplayScore.WIN, DisplayScore.ZERO),
            (DisplayScore.WIN, DisplayScore.ZERO),
        ]
        self.assertEqual(winner, expected_winner)
        self.assertEqual(scores, expected_scores)

    def test_players_cannot_play_after_winning_set(self):
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(0, 4)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.set.add_points(4, 0)
        self.assertRaises(ValueError, self.set.add_points, 4, 0)