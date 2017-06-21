class Pris:
    def __init__(self, currentPris = "0", forjePris ="0"):
        self.currentPris = currentPris
        self.forjePris = forjePris

    @property
    def getCurrentPris(self):
        return self.__currentPris

    @getCurrentPris.setter
    def setCurrentPris(self, value):
        self.__currentPris = value

    @property
    def getForjePris(self):
        return self.__currentPris

    @getForjePris.setter
    def setForjePris(self, value):
        self.__forjePris = value