import unittest

from tennis import Set, DisplayScore


class Test(unittest.TestCase):
    def setUp(self):
        self.set: Set = Set()

    def test_points_winned_must_be_positive(self):
        self.assertRaises(ValueError, self.set.add_points, -2, 1)

    def test_scores_must_have_valid_values_when_deuce_activated(self):
        self.assertRaises(ValueError, self.set.add_points, 7, 4)

    def test_scores_must_have_valid_values_when_deuce_not_activated(self):
        self.assertRaises(ValueError, self.set.add_points, 6, 2)

    def test_player1_scores_fifteen(self):
        self.set.add_points(1, 0)
        scores = self.set.get_display_scores()
        expected_scores = (DisplayScore.FIFTEEN, DisplayScore.ZERO)
        self.assertEqual(scores, expected_scores)

    def test_player1_and_player2_both_score_thirty(self):
        self.set.add_points(2, 2)
        scores = self.set.get_display_scores()
        expected_scores = (DisplayScore.THIRTY, DisplayScore.THIRTY)
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_without_deuce(self):
        self.set.add_points(4, 2)
        scores = self.set.get_display_scores()
        expected_scores = (DisplayScore.WIN, DisplayScore.THIRTY)
        self.assertEqual(scores, expected_scores)

    def test_player1_has_advantage(self):
        self.set.add_points(4, 3)
        scores = self.set.get_display_scores()
        expected_scores = (DisplayScore.ADVANTAGE, DisplayScore.DEUCE)
        self.assertEqual(scores, expected_scores)

    def test_player1_has_advantage_and_large_score(self):
        self.set.add_points(10, 9)
        scores = self.set.get_display_scores()
        expected_scores = (DisplayScore.ADVANTAGE, DisplayScore.DEUCE)
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_with_deuce(self):
        self.set.add_points(5, 3)
        scores = self.set.get_display_scores()
        expected_scores = (DisplayScore.WIN, DisplayScore.DEUCE)
        self.assertEqual(scores, expected_scores)

    def test_player1_wins_with_deuce_and_large_score(self):
        self.set.add_points(10, 8)
        scores = self.set.get_display_scores()
        expected_scores = (DisplayScore.WIN, DisplayScore.DEUCE)
        self.assertEqual(scores, expected_scores)