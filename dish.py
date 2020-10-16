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

    def add_unwanted_ingredients(self, ingreident):
        self.unwanted_ingredients.add(ingreident)
        self.ingredients.remove(ingreident)
