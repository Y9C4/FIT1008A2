from __future__ import annotations
from constants import PlayerPosition, PlayerStats
from data_structures.hash_table import LinearProbeTable
from data_structures.referential_array import ArrayR
from hashy_perfection_table import HashyPerfectionTable


class Player:

    def __init__(self, name: str, position: PlayerPosition, age: int) -> None:
        """
        Constructor for the Player class
        name - a string representing the name of the player. The name is given in the init method. You can assume the name is unique.

        position - a position is given by the PlayerPosition in constants.py. The position is given in the init method. 

        age - an integer representing the age of the player (must be 18 or higher). The age is given in the  init method. 

        statistics - a data structure that holds the values of statistics relevant to the player. A list of statistics is given in the constants file as PlayerStats and on __init__ these stats should all be set to 0.

        Args:
            name (str): The name of the player
            position (PlayerPosition): The position of the player
            age (int): The age of the player

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:

        """
        self.name = name
        self.position = position
        self.age = age
        self.statistics = HashyPerfectionTable() #still needs to be swapped with one of the custom hash tables
            
        for stat in PlayerStats:
            if stat.value == "Last Five Results":
                self.statistics[stat.value] = ArrayR(5)
            else:
                self.statistics[stat.value] = 0
            


    def reset_stats(self) -> None:
        """
        resets all  PlayerStats stats to 0. identical to __init__

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:

        """       
        for stat in PlayerStats:
            self.statistics[stat.value] = 0

    def get_name(self) -> str:
        """
        returns the name of the player.

        Returns:
            str: The name of the player

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return self.name

    def get_position(self) -> PlayerPosition:
        """
        returns the position of the player.

        Returns:
            PlayerPosition: The position of the player

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return self.position

    def get_statistics(self):
        """
        returns the statistics of the player.

        Returns:
            statistics: The players' statistics

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return self.statistics



    def __setitem__(self, statistic: PlayerStats, value: int) -> None:
        """
        Set the value of the player's stat based on the key that is passed.
        updates the value of the statistic passed as  statistic.

        Args:
            statistic (PlayerStat): The key of the stat
            value (int): The value of the stat

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        if type(statistic) == PlayerStats:
            statistic = statistic.value
            
        self.statistics[statistic] = value

    def __getitem__(self, statistic: PlayerStats) -> int:
        """
        Get the value of the player's stat based on the key that is passed.
        returns the value of the statistic passed as  key. 

        Args:
            statistic (PlayerStat): The key of the stat

        Returns:
            int: The value of the stat

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return self.statistics[statistic.value]

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the player object.

        Complexity:
            Analysis not required.
        """
        return (self.name, self.age, self.position, self.statistics)

    def __repr__(self) -> str:
        """Returns a string representation of the Player object.
        Useful for debugging or when the Player is held in another data structure."""
        return str(self)
