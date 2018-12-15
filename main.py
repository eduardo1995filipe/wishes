import WishManager


def main():

        wish_manager = WishManager.WishManager()

        exit = False
        while exit is False:
                print("")
                print("Main Menu:")
                print("1 - Check wishes")
                print("2 - Add new wish")
                print("3 - Unwish")
                print("4 - Exit")
                value = int(input("Choose an option:"))
                if value == 4:
                        exit = True
                elif value == 1:
                        wish_list = wish_manager.getAllWishes()
                        for wish in wish_list:
                                print(wish)
                elif value == 2:
                        description = input("insert a description: ")
                        value = float(input("insert a value: "))
                        savings = float(input("insert your savings for this wish(pass if you don't have savings yet): "))
                        wish_manager.createWish(description = description, value = value, savings = savings)
                        print("Expense successfully added :D")
                elif value == 3:
                        wish_list = wish_manager.getAllWishes()
                        for wish in wish_list:
                                print(wish)
                        id = int(input("insert the id of the wish that you want to unwish: "))
                        wish_manager.removeWishById(id)
                        print("successfully unwished!")

                        


if __name__ == "__main__":
    print("Welcome to wishes! Post your wish here and amount money to buy it! :D")
    main()