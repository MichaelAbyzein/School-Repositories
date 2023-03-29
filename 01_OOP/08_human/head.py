from eye import Eye
from mouth import Mouth

class Head:
    def __init__(self, InfoHuman):
        self.eyes = Eye()
        self.mouth = Mouth(InfoHuman)