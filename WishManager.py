import Wish 

class WishManager:

    def __init__(self):
        self.wish_list = []

    def createWish(self, description, value, savings = None):
        if savings is None:
            new_wish = Wish.Wish(self.getNextID(), description, float(value))
        else:
            new_wish = Wish.Wish(self.getNextID(), description, float(value), float(savings))
        self.wish_list.append(new_wish)

    def getAllWishes(self):
        return self.wish_list

    def removeWishById(self, id):
        for wish in self.wish_list:
            if wish.id == id:
                self.wish_list.remove(wish)
                return

    def getNextID(self):
        max_id = 0  
        for element in self.wish_list:
            if element.id > max_id:
                max_id = element.id
        return (max_id + 1)
