from Player import Player
from HumanPlayer import HumanPlayer
from DuelField import DuelField

player_1 = HumanPlayer("Berkay")
player_2 = Player("AI_0")

game = DuelField(player_1, player_2)

game.startFight(1)
