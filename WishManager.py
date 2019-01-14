import Wish 

class WishManager:

    def __init__(self):
        self.wish_list = []
        self.filename = "wishes.txt"
        self.loadWishes()

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

    def loadWishes(self):
        loaded_wish_list = []
        try:
            file = open(self.filename, "r")
        except FileNotFoundError:
            file = open(self.filename, "w+")
        for line in file:
            wish_array = line.split(";")
            new_wish = Wish.Wish(int(wish_array[0]), wish_array[1], float(wish_array[2]), float(wish_array[3]))
            loaded_wish_list.append(new_wish)
        self.wish_list = loaded_wish_list
        file.close()
        return
        
    
    def commitChanges(self):
        file = open(self.filename, "w")
        for wish in self.wish_list:
            file.write(str(wish.id) + ";" + wish.description + ";" +  str(wish.value) + ";" + str(wish.savings) +"\n")
        file.close()
        return

    def changeSavingsById(self,id, new_savings):
        for wish in self.wish_list:
            if wish.id == id:
                wish.savings = wish.savings + new_savings
                return True
        return False