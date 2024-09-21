from __future__ import annotations
from data_structures.bset import BSet
from data_structures.referential_array import ArrayR
from data_structures.array_sorted_list import ArraySortedList
from data_structures.linked_list import LinkedList
from game_simulator import GameSimulator
from dataclasses import dataclass
from team import Team
from typing import Generator, Union


@dataclass
class Game:
    """
    Simple container for a game between two teams.
    Both teams must be team objects, there cannot be a game without two teams.

    Note: Python will automatically generate the init for you.
    Use Game(home_team: Team, away_team: Team) to use this class.
    See: https://docs.python.org/3/library/dataclasses.html
    """
    home_team: Team = None
    away_team: Team = None


class WeekOfGames:
    """
    Simple container for a week of games.

    A fixture must have at least one game.
    """

    def __init__(self, week: int, games: ArrayR[Game]) -> None:
        """
        Container for a week of games.

        Args:
            week (int): The week number.
            games (ArrayR[Game]): The games for this week.
        """
        self.games: ArrayR[Game] = games
        self.week: int = week
        self._current_index = 0 #property used for iterate and next method

    def get_games(self) -> ArrayR:
        """
        Returns the games in a given week.

        Returns:
            ArrayR: The games in a given week.

        Complexity:
        Best Case Complexity: O(1)
        Worst Case Complexity: O(1)
        """
        return self.games

    def get_week(self) -> int:
        """
        Returns the week number.

        Returns:
            int: The week number.

        Complexity:
        Best Case Complexity: O(1)
        Worst Case Complexity: O(1)
        """
        return self.week

    def __iter__(self):
        """
        Complexity:
        Best Case Complexity:
        Worst Case Complexity:
        """
        self._current_index = 0
        return self
        

    def __next__(self):
        """
        Complexity:
        Best Case Complexity:
        Worst Case Complexity:
        """
        if self._current_index >= len(self.games):
            raise StopIteration  # No more games to iterate over
        game = self.games[self._current_index]
        self._current_index += 1
        return game



class Season:

    def __init__(self, teams: ArrayR[Team]) -> None:
        """
        Initializes the season with the following attributes:

            leaderboard : A data structure that holds; by default in descending order of points; the teams taking part in the season. If there is a tie on points, you must break the tie by the goal_difference of the team. If there is still a tie, then it should be broken by goals_for of the team. If there is still a tie, then you must order the teams alphabetically, however, if the name sorts it, this MUST be done in an ascending order. During initialisation, the leaderboard must contain all teams and they should be sorted by name (as all the other stats are 0 or None)

            schedule : A data structure that will hold the randomized schedule of the season. 
            NOTE - The logic to generate this has already been done for you. You just need to call the method _generate_schedule() while creating this instance variable and then store the returned ArrayR into an appropriate data structure (you cannot store it as an ArrayR).

            teams - The original ArrayR of teams participating in the season.
        
        Args:
            teams (ArrayR[Team]): The teams played in this season.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.leaderboard = ArraySortedList(10)
        for team in teams: #adds team at the correct index
            self.leaderboard.add(team)
        
        self.teams = teams
        
        schedule_array = self._generate_schedule() #generate schedule
        self.schedule = LinkedList()

        for week_ind in range(0, len(schedule_array)):
            gameweek = WeekOfGames(week_ind, schedule_array[week_ind])
            self.schedule.append(gameweek)

    def _generate_schedule(self) -> ArrayR[ArrayR[Game]]:
        """
        Generates a schedule by generating all possible games between the teams.

        Return:
            ArrayR[ArrayR[Game]]: The schedule of the season.
                The outer array is the weeks in the season.
                The inner array is the games for that given week.

        Complexity:
            Best Case Complexity: O(N^2) where N is the number of teams in the season.
            Worst Case Complexity: O(N^2) where N is the number of teams in the season.
        """
        num_teams: int = len(self.teams)
        weekly_games: list[ArrayR[Game]] = []
        flipped_weeks: list[ArrayR[Game]] = []
        games: list[Game] = []

        # Generate all possible matchups (team1 vs team2, team2 vs team1, etc.)
        for i in range(num_teams):
            for j in range(i + 1, num_teams):
                games.append(Game(self.teams[i], self.teams[j]))

        # Allocate games into each week ensuring no team plays more than once in a week
        week: int = 0
        while games:
            current_week: list[Game] = []
            flipped_week: list[Game] = []
            used_teams: BSet = BSet()

            week_game_no: int = 0
            for game in games[:]:  # Iterate over a copy of the list
                if game.home_team.get_number() not in used_teams and game.away_team.get_number() not in used_teams:
                    current_week.append(game)
                    used_teams.add(game.home_team.get_number())
                    used_teams.add(game.away_team.get_number())

                    flipped_week.append(Game(game.away_team, game.home_team))
                    games.remove(game)
                    week_game_no += 1

            weekly_games.append(ArrayR.from_list(current_week))
            flipped_weeks.append(ArrayR.from_list(flipped_week))
            week += 1

        return ArrayR.from_list(weekly_games + flipped_weeks)

    def simulate_season(self) -> None:
        """
        Simulates the season.

        Complexity:
            Assume simulate_game is O(1)
            Remember to define your variables and their complexity.

            Best Case Complexity:
            Worst Case Complexity:
        """

        results_list = LinkedList()
        game_iterator = self.get_next_game()
        
        for game in game_iterator:
            results_list.append(GameSimulator.simulate(game.home_team, game.away_team))
        
        for result in results_list:
            self.leaderboard.index()
            if result["Home Goals"] > result["Away Goals"]:
            
            elif result["Home Goals"] < result["Away Goal"]:
                winner = "away"
            else:
                winner = "draw"
            
        
    def delay_week_of_games(self, orig_week: int, new_week: Union[int, None] = None) -> None:
        """
        Delay a week of games from one week to another.

        Args:
            orig_week (int): The original week to move the games from.
            new_week (Union[int, None]): The new week to move the games to. If this is None, it moves the games to the end of the season.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        delayed_week = self.schedule[orig_week-1]
        self.schedule.remove(delayed_week)

        if new_week == None:
            new_week = len(self.schedule)
        else:
            new_week -= 1
        
        self.schedule.insert(new_week, delayed_week)


    def get_next_game(self) -> Union[Generator[Game], None]:
        """
        Gets the next game in the season.

        Returns:
            Game: The next game in the season.
            or None if there are no more games left.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """

        for week in self.schedule:
            for game in week:
                yield game

    def get_leaderboard(self) -> ArrayR[ArrayR[Union[int, str]]]:
        """
        Generates the final season leaderboard.

        Returns:
            ArrayR(ArrayR[ArrayR[Union[int, str]]]):
                Outer array represents each team in the leaderboard
                Inner array consists of 10 elements:
                    - Team name (str)
                    - Games Played (int)
                    - Points (int)
                    - Wins (int)
                    - Draws (int)
                    - Losses (int)
                    - Goals For (int)
                    - Goals Against (int)
                    - Goal Difference (int)
                    - Previous Five Results (ArrayR(str)) where result should be WIN LOSS OR DRAW

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def get_teams(self) -> ArrayR[Team]:
        """
        Returns:
            PlayerPosition (ArrayR(Team)): The teams participating in the season.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return self.teams

    def __len__(self) -> int:
        """
        Returns the number of teams in the season.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return len(self.teams)

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the season object.

        Complexity:
            Analysis not required.
        """
        return ""

    def __repr__(self) -> str:
        """Returns a string representation of the Season object.
        Useful for debugging or when the Season is held in another data structure."""
        return str(self)
