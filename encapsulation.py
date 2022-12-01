
# Protected class
class Character:
    def __init__(self):
        self._inventory = Inventory()

# Private class
class Inventory:
    def __init__(self):
        self.__goldTotal = 1000
    # Returns integer value of __goldTotal
    def getGoldTotal(self):
        return self.__goldTotal
    # Takes integer newTotal and assigns it to __goldTotal
    def setGoldTotal(self, newTotal):
        self.__goldTotal = newTotal

character = Character()

# Prints __goldTotal from Inventory that was instantiated inside our character class
print('Total gold in inventory:'+str(character._inventory.getGoldTotal()))

# Sets a new __goldTotal passing integer value of 2000
character._inventory.setGoldTotal(2000) 

# Print __goldTotal again to see the result of setting a new __goldTotal
print('New total gold in inventory:'+str(character._inventory.getGoldTotal()))
