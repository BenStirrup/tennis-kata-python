from typing import Tuple, List, Optional

class DisplayScore:
    ZERO: str = "0"
    FIFTEEN: str = "15"
    THIRTY: str = "30"
    FORTY: str = "40"
    DEUCE: str = "DEUCE"
    ADVANTAGE: str = "ADVANTAGE"
    WIN: str = "WIN"


class Game:
    def __init__(self) -> None:
        self.score1: int = 0
        self.score2: int = 0
        self.score_diff: int = 0
        self.display_score1: str = DisplayScore.ZERO
        self.display_score2: str = DisplayScore.ZERO
        self.is_deuce_activated: bool = False

    def get_display_scores(self) -> Tuple[str, str]:
        return self.display_score1, self.display_score2

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

        self.set_display_scores()

    def set_display_scores(self):

        if not self.is_deuce_activated:
            if self.score1 == 1:
                self.display_score1 = DisplayScore.FIFTEEN
            if self.score2 == 1:
                self.display_score2 = DisplayScore.FIFTEEN

            if self.score1 == 2:
                self.display_score1 = DisplayScore.THIRTY
            if self.score2 == 2:
                self.display_score2 = DisplayScore.THIRTY

            if self.score1 == 3:
                self.display_score1 = DisplayScore.FORTY
            if self.score2 == 3:
                self.display_score2 = DisplayScore.FORTY

            if self.score1 == 4:
                self.display_score1 = DisplayScore.WIN
            if self.score2 == 4:
                self.display_score2 = DisplayScore.WIN

        else:
            self.display_score1 = DisplayScore.DEUCE
            self.display_score2 = DisplayScore.DEUCE

            is_player1_winning: bool = self.score1 > self.score2
            if self.score_diff == 1:
                if is_player1_winning:
                    self.display_score1 = DisplayScore.ADVANTAGE
                else:
                    self.display_score2 = DisplayScore.ADVANTAGE

            if self.score_diff == 2:
                if is_player1_winning:
                    self.display_score1 = DisplayScore.WIN
                else:
                    self.display_score2 = DisplayScore.WIN


class Set:
    def __init__(self, player1, player2) -> None:
        self.player1: str = player1
        self.player2: str = player2
        self.winner: Optional[str] = None
        self.game: Game = Game()
        self.games_won_by_player_1: int = 0
        self.games_won_by_player_2: int = 0
        self.display_scores: List[Tuple[str, str]] = []
        self.is_seventh_game_required: bool = False

    def add_points(self, points1: int, points2: int):
        if self.winner:
            raise ValueError(
                "The set is already finished! The winner is " + self.winner
            )

        self.game.add_points(points1, points2)
        result1, result2 = self.game.display_score1, self.game.display_score2

        game_won = False
        if result1 == DisplayScore.WIN:
            game_won = True
            self.games_won_by_player_1 += 1
            if (
                not self.is_seventh_game_required and self.games_won_by_player_1 == 6
            ) or (self.is_seventh_game_required and self.games_won_by_player_1 == 7):
                self.winner = self.player1

        elif result2 == DisplayScore.WIN:
            game_won = True
            self.games_won_by_player_2 += 1
            if (
                not self.is_seventh_game_required and self.games_won_by_player_2 == 6
            ) or (self.is_seventh_game_required and self.games_won_by_player_2 == 7):
                self.winner = self.player2

        if game_won:
            self.display_scores.append((result1, result2))
            self.game = Game()

        if self.games_won_by_player_1 >= 5 and self.games_won_by_player_2 >= 5:
            self.is_seventh_game_required = True

    def get_current_game_display_scores(self) -> Tuple[str, str]:
        return self.game.get_display_scores()

    def get_previous_games_display_scores(self) -> List[Tuple[str, str]]:
        return self.display_scores

    def get_winner(self) -> Optional[str]:
        return self.winner
