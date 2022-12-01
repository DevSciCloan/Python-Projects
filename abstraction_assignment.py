# Import Abstract Base Class
from abc import ABC, abstractmethod
        
class Inventory(ABC):
    def __init__(self):
        self.__inventory = None
    def confirmTrade(self, items):
        print('Trade accepted!')
    def getInv(self):
        return self.__inventory
    def setInv(self,inv):
        self.__inventory = inv

    # Abstract method used to update inventory
    @abstractmethod
    def updateInventory(self, items):
        pass
# Gets inventory as a dict and deducts the ammount of items from each key, value then sets the new inv 
class give(Inventory):
    def updateInventory(self, items):
        toUpdate = self.getInv()
        for k,v in items.items():
            toUpdate[k] = items[k] - toUpdate[k] 
        self.setInv(toUpdate)
        print('You are giving: {}'.format(items))
        
# Gets inventory as a dict and adds the values for each kay, value pair that was subtracted from other player     
class receive(Inventory):
    def updateInventory(self, items):
        toUpdate = self.getInv()
        for i in items:
            toUpdate[i] += items[i]
        self.setInv(toUpdate)
        print('You received: {}'.format(items))
        
# Instantiate player that is giving items
character1 = give()
character1.setInv({'food': 2,'gold': 1000,'weapons': 1})

# Instantiate player receiving items
character2 = receive()
character2.setInv({'food': 3,'gold': 2000,'weapons': 1})

print('Player 1 you have: {}'.format(list(character1.getInv().items())))

# Creating a dict for the ammount of items in each key, value pair to be traded
offer = {'food': 2,'gold': 1000,'weapons': 1}

# Update inventory for player 1
character1.updateInventory(offer)
character1.confirmTrade(offer)
# Display new inventory to user
print('Player 1 you now have: {}'.format(list(character1.getInv().items())))

print('Player 2 you have: {}'.format(list(character2.getInv().items())))

# Update inventory for player 2
character2.updateInventory(offer)
character2.confirmTrade(offer)
print('Player 2, you now have: {}'.format(list(character2.getInv().items())))
