import ingredient


class Dish:
    def __init__(self, name, menu_number, ingredients, price, unwanted_ingredients):
        self.name = name
        self.menu_number = menu_number
        self.allergens = []
        self.ingredients = ingredients
        self.price = price
        self.unwanted_ingredients = unwanted_ingredients
        for element in ingredients:
            if element.is_allergen():
                self.allergens.append(element)

    # getters

    # get_name
    # returns the name of the dish (string)

    def get_name(self):
        return self.name

    # get_menu_number
    # returns the menu number (integer)

    def get_menu_number(self):
        return self.menu_number

    # get_allergens
    # returns the allergens(set)

    def get_allergens(self):
        return self.allergens

    # get_ingredients
    # returns the ingredients(set)

    def get_ingredients(self):
        return self.ingredients

    # get_unwanted_ingredients
    # returns the unwanted ingredients(set)

    def get_unwanted_ingredients(self):
        return self.unwanted_ingredients

    # get_price
    # returns the price(double)

    def get_price(self):
        return self.price

    # add_unwanted_ingredients
    # adds an ingredient to unwanted ingredients and removes ingredient from ingredients
    # checks if inputted ingredient is already in list. If not, return 0, if true, return 1

    def add_unwanted_ingredients(self, unwanted_ingredient):
        if unwanted_ingredient not in self.ingredients and unwanted_ingredient not in self.unwanted_ingredients:
            return -1
        # if ingredient already in unwanted list, return 0 (already done)
        elif unwanted_ingredient in self.unwanted_ingredients:
            return 0
        # else, add in ingredient
        else:
            self.unwanted_ingredients.append(unwanted_ingredient)
            self.ingredients.remove(unwanted_ingredient)
            return 0

    # remove_unwanted_ingredient
    def remove_unwanted_ingredients(self, unwanted_ingredient):
        if unwanted_ingredient not in self.ingredients or unwanted_ingredient not in self.unwanted_ingredients:
            return -1
        # if ingredient already in unwanted list, return 0 (already done)
        elif unwanted_ingredient in self.ingredients:
            return 0
        # else, add in ingredient
        else:
            self.unwanted_ingredients.remove(unwanted_ingredient)
            self.ingredients.append(unwanted_ingredient)
            return 0

    # to string

    def to_string(self):
        s = self.name
        return s

    # equal

    def __eq__(self, other):
        return self.name == other.name and self.menu_number == other.menu_number and self.price == other.price


