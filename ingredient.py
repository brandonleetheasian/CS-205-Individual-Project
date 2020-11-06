class Ingredient:
    # initializer

    def __init__(self, name, allergen):
        self.name = name
        self.allergen = allergen

    # returns name

    def get_name(self):
        return self.name

    # returns the allergen

    def get_allergen(self):
        return self.allergen
