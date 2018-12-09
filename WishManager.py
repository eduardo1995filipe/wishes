import Wish 

class WishManager:

    def __init__(self):
        self.wish_list = []

    def createWish(self, description, value, savings = None):
        if savings is None:
            new_wish = Wish.Wish(description ,value)
        else:
            new_wish = Wish.Wish(description ,value, savings)
        self.wish_list.append(new_wish)

    def getAllWishes(self):
        return self.wish_list