from __future__ import annotations
from data_structures.referential_array import ArrayR
from constants import GameResult, PlayerPosition, PlayerStats, TeamStats
from player import Player
from typing import Collection, Union, TypeVar
from data_structures.hash_table import LinearProbeTable
from data_structures.linked_list import LinkedList
from data_structures.linked_queue import LinkedQueue

T = TypeVar("T")


class Team:
    team_num = 1
    def __init__(self, team_name: str, players: ArrayR[Player]) -> None:
        """
        Constructor for the Team class
        number - A unique number for this team. The first team number should be 1 (then 2, and so on).

        name - a string that refers to the team's name. The name is given in the init method. You can assume the name is unique.

        statistics - a data structure that contains statistics related to the Team class. These are similar (but not the same as the player stats).  A list of statistics is given in the constants file as TeamStats and on __init__ these stats should all be set to 0 (with the exception of the LAST_FIVE_RESULTS statistic, which should be initialised to an empty container of the ADT of your choice).

        players - a collection of Player objects grouped by PlayerPosition, initially provided to __init__  as an ArrayR of players and then stored with an appropriate ADT to ensure they appear by the player's position (see image below). For example, all goalkeepers are saved together and all midfielders are saved together. To see the possible positions, you can refer to the PlayerPosition enum. You can assume that the enum is exhaustive and we will never have another position that doesn't exist in the enum. 
        HINT - To get the number of values that exist in an enum class EnumClass, you can call len(EnumClass)
        NOTE - The order of the players is important. For example - if you get two goalkeepers, where gk1 arrives before gk2 to the team, then gk1 needs to be before gk2. 
        See an example of the structure below:
        Given an collection of players and their positions in brackets for visual purposes.

        Args:
            team_name (str): The name of the team
            players (ArrayR[Player]): The players of the team

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.name = team_name
        self.number = Team.team_num
        Team.team_num += 1
        self.statistics = LinearProbeTable()
        self.num_players = 0
        
        for stat in TeamStats:
            if stat.value == "Last Five Results":
                self.statistics[stat.value] = LinkedQueue()
            else:
               self.statistics[stat.value] = 0
        
        self.players = LinearProbeTable()
        
        for position in PlayerPosition: #create the player position arrays
            self.players[position.value] = LinkedList()
        
        for player in players: #adds the player in the correct position.
            self.add_player(player)
        

    def reset_stats(self) -> None:
        """
        Resets all the statistics of the team to the values they were during init.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        for stat in TeamStats:
            if stat.value == "Last Five Results":
                self.statistics[stat.value] = LinkedQueue()
            else:
               self.statistics[stat.value] = 0

    def add_player(self, player: Player) -> None:
        """
        Adds a player to the team.

        Args:
            player (Player): The player to add

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.players[player.position.value].append(player)
        self.num_players += 1

    def remove_player(self, player: Player) -> None:
        """
        Removes a player from the team.

        Args:
            player (Player): The player to remove

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.players[player.position.value].delete_at_index(self.players[player.position.value].index(player))
        self.num_players -= 1
        

    def get_number(self) -> int:
        """
        Returns the number of the team.

        Complexity:
            Analysis not required.
        """
        return self.number

    def get_name(self) -> str:
        """
        Returns the name of the team.

        Complexity:
            Analysis not required.
        """
        return self.name

    def get_players(self, position: Union[PlayerPosition, None] = None) -> Union[Collection[Player], None]:
        """
        Returns the players of the team that play in the specified position.
        If position is None, it should return ALL players in the team.
        You may assume the position will always be valid.
        Args:
            position (Union[PlayerPosition, None]): The position of the players to return

        Returns:
            Collection[Player]: The players that play in the specified position
            held in a valid data structure provided to you within
            the data_structures folder this includes the ArrayR
            which was previously prohibited.

            None: When no players match the criteria / team has no players

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        
        return_players = LinkedList()

        if position == None:
            for pos in PlayerPosition:
                for player in self.players[pos.value]:
                    return_players.append(player)

        else:
            return_players = self.players[position.value]
        
        if len(return_players) == 0:
            return None
        else:
            return return_players

    def get_statistics(self):
        """
        Get the statistics of the team

        Returns:
            statistics: The teams' statistics

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return self.statistics

    def get_last_five_results(self) -> Union[Collection[GameResult], None]:
        """
        Returns the last five results of the team.
        If the team has played less than five games,
        return all the result of all the games played so far.

        For example:
        If a team has only played 4 games and they have:
        Won the first, lost the second and third, and drawn the last,
        the array should be an array of size 4
        [GameResult.WIN, GameResult.LOSS, GameResult.LOSS, GameResult.DRAW]

        **Important Note:**
        If this method is called before the team has played any games,
        return None the reason for this is explained in the specefication.

        Returns:
            Collection[GameResult]: The last five results of the team
            or
            None if the team has not played any games.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        if len(self.statistics["Last Five Results"]) < 1:
            return None
        else:
            return self.statistics["Last Five Results"]

    def get_top_x_players(self, player_stat: PlayerStats, num_players: int) -> list[tuple[int, str, Player]]:
        """
        Note: This method is only required for FIT1054 students only!

        Args:
            player_stat (PlayerStats): The player statistic to use to order the top players
            num_players (int): The number of players to return from this team

        Return:
            list[tuple[int, str, Player]]: The top x players from this team
        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __setitem__(self, statistic: TeamStats, value: int) -> None:
        """
        __setitem__(self, statistic: TeamStats, value: int) - this method updates the value of the statistic that is passed as the statistic. Consider the cascading effect of updating a statistic as well. For example - if we are updating the number of wins, then you need to update the points as well as the last 5 games statistic as well. 
        For example - if statistic is WINS and the value being passed is n+1
         n+1 and the current value of WINS for the team is 
        n
        n, then we do the following:

        Update the number of WINS by 1

        Update the number of GAMES_PLAYED by 1 (this should be applied to the team and every player in the team).

        Update the number of POINTS by adding the value of GameResult.WIN.value (which is set to 3 in the scaffold)

        Add the result to the LAST_FIVE_RESULTS as the latest result.
        NOTE - You can assume that setitem will always be additive, i.e. we will never call this method to 'reduce' the statistics in any way, it will always add to the existing value.

        You should also consider updating GOAL_DIFFERENCE, when updating GOALS_FOR or GOALS_AGAINST.

        You can assume that setitem will never be called on GOAL_DIFFERENCE , LAST_FIVE_RESULTS , GAMES_PLAYED , POINTS directly as these get set as a cascading effect of other statistics.

        Args:
            statistic (TeamStats): The statistic to update
            value (int): The new value of the statistic

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """

        if statistic.value == "Games Played":
            # Your code for handling Games Played
            self.statistics[statistic.value] = value

        elif statistic.value == "Points":
            # Your code for handling Points
            self.statistics[statistic.value] = value

        elif statistic.value == "Wins":
            # Your code for handling Wins
            temp_list = self.statistics["Last Five Results"]
            if len(temp_list) > 4:
                temp_list.serve()
            
            temp_list.append(GameResult(3))
            self.statistics["Games Played"] += 1
            self.statistics["Points"] += 3
            self.statistics[statistic.value] = value

        elif statistic.value == "Draws":
            # Your code for handling Draws
            temp_list = self.statistics["Last Five Results"]
            if len(temp_list) > 4:
                temp_list.serve()
            
            temp_list.append(GameResult(1))
            self.statistics["Games Played"] += 1
            self.statistics["Points"] += 1
            self.statistics[statistic.value] = value

        elif statistic.value == "Losses":
            # Your code for handling Losses
            temp_list = self.statistics["Last Five Results"]
            if len(temp_list) > 4:
                temp_list.serve()
            self.statistics["Games Played"] += 1
            temp_list.append(GameResult(0))
            
            self.statistics[statistic.value] = value

        elif statistic.value == "Goals For":
            # Your code for handling Goals For
            self.statistics[statistic.value] = value
            self.statistics["Goals Difference"] = self.statistics["Goals For"] - self.statistics["Goals Against"]

        elif statistic.value == "Goals Against":
            # Your code for handling Goals Against
            self.statistics[statistic.value] = value
            self.statistics["Goals Difference"] = self.statistics["Goals For"] - self.statistics["Goals Against"]

        elif statistic.value == "Goals Difference": 
            # Your code for handling Goals Difference
            self.statistics[statistic.value] = value

    def __getitem__(self, statistic: TeamStats) -> int:
        """
        Returns the value of the specified statistic.

        Args:
            statistic (TeamStats): The statistic to return

        Returns:
            int: The value of the specified statistic

        Raises:
            ValueError: If the statistic is invalid

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return self.statistics[statistic.value]

    def __len__(self) -> int:
        """
        Returns the number of players in the team.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        player_list = self.get_players()
        if player_list == None:
            return 0
        else:
            return len(player_list)

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the team object.

        Complexity:
            Analysis not required.
        """
        return ""

    def __repr__(self) -> str:
        """Returns a string representation of the Team object.
        Useful for debugging or when the Team is held in another data structure."""
        return str(self)