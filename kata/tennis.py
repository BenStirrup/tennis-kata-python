from typing import Tuple


class DisplayScore:
    ZERO: str = "0"
    FIFTEEN: str = "15"
    THIRTY: str = "30"
    FORTY: str = "40"
    DEUCE: str = "DEUCE"
    ADVANTAGE: str = "ADVANTAGE"
    WIN: str = "WIN"


class Set:
    def __init__(self) -> None:
        self.score1: int = 0
        self.score2: int = 0
        self.score_diff: int = 0
        self.is_deuce_activated: bool = False

    def add_points(self, points1: int, points2: int):
        if points1 < 0 or points2 < 0:
            raise ValueError("Points winned must be positive")

        self.score1 += points1
        self.score2 += points2
        self.score_diff = abs(self.score1 - self.score2)

        if self.score1 >= 3 and self.score2 >= 3:
            self.is_deuce_activated = True

        if self.is_deuce_activated and self.score_diff > 2:
            raise ValueError(
                "Points difference must be inferior or equal to 2 when deuce activated"
            )

        if (self.score1 > 4 and self.score2 < 3) or (
            self.score2 > 4 and self.score1 < 3
        ):
            raise ValueError(
                "A player's points cannot be above 4 if the other player's points is less than 3"
            )

    def get_display_scores(self) -> Tuple[str, str]:

        if not self.is_deuce_activated:
            display_score1 = DisplayScore.ZERO
            display_score2 = DisplayScore.ZERO

            if self.score1 == 1:
                display_score1 = DisplayScore.FIFTEEN
            if self.score2 == 1:
                display_score2 = DisplayScore.FIFTEEN

            if self.score1 == 2:
                display_score1 = DisplayScore.THIRTY
            if self.score2 == 2:
                display_score2 = DisplayScore.THIRTY

            if self.score1 == 3:
                display_score1 = DisplayScore.FORTY
            if self.score2 == 3:
                display_score2 = DisplayScore.FORTY

            if self.score1 == 4:
                display_score1 = DisplayScore.WIN
            if self.score2 == 4:
                display_score2 = DisplayScore.WIN

        else:
            display_score1 = DisplayScore.DEUCE
            display_score2 = DisplayScore.DEUCE

            is_player1_winning: bool = self.score1 > self.score2
            if self.score_diff == 1:
                if is_player1_winning:
                    display_score1 = DisplayScore.ADVANTAGE
                else:
                    display_score2 = DisplayScore.ADVANTAGE

            if self.score_diff == 2:
                if is_player1_winning:
                    display_score1 = DisplayScore.WIN
                else:
                    display_score2 = DisplayScore.WIN

        return display_score1, display_score2
