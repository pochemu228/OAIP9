class Chest():
    def __init__(self, color, hammer, screwdriver, nails):
        self.__color = color
        self.__hammer = hammer
        self.__screwdriver = screwdriver
        self.__nails = nails
        self.__position = False

    def start(self):
        self.__position = True
        print('Сундук открыт')

    def stop(self):
        self.__position = False
        print('Сундук закрыт')

    def public(self):
        pass

    def _private(self):
        pass

    def __protected(self):
        pass

Chest = Chest('gold', 20, 15, 10)
Chest.start()
Chest.stop()
