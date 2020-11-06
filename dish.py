class Dish:
    def __init__(self, name, menu_number, allergens, ingredients, price, unwanted_ingredients):
        self.name = name
        self.menu_number = menu_number
        self.allergens = allergens
        self.ingredients = ingredients
        self.price = price
        self.unwanted_ingredients = unwanted_ingredients

    # getters

    # returns the name of the dish (string)

    def get_name(self):
        return self.name

    # returns the menu number (integer)

    def get_menu_number(self):
        return self.menu_number

    # returns the allergens(set)

    def get_allergens(self):
        return self.allergens

    # returns the ingredients(set)

    def get_ingredients(self):
        return self.ingredients

    # returns the price(double)

    def get_price(self):
        return self.price

    # adds an ingredient to unwanted ingredients and removes ingredient from ingredients
    # checks if inputted ingredient is already in list. If not, return 0, if true, return 1

    def add_unwanted_ingredients(self, ingredient):
        # if ingredient already in unwanted list, return -1
        if ingredient in self.unwanted_ingredients:
            return -1
        # else, add in ingredient
        else:
            self.unwanted_ingredients.append(ingredient)
            self.ingredients.remove(ingredient)
            return 0

    def remove_unwanted_ingredients(self, ingredient):
        # if ingredient not in unwanted list, return -1
        if ingredient not in self.unwanted_ingredients:
            return -1
        # else, remove ingredient and return 0
        else:
            self.unwanted_ingredients.remove(ingredient)
            self.ingredients.append(ingredient)




