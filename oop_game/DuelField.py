from Field import Field
from Team import Team

class DuelField(Field):
    def __init__(self, player1, player2):
        super().__init__( Team("A", [player1]), Team("B", [player2]) )