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

    def to_string(self):
        s = self.name
        return s

    def __eq__(self, other):
        return self.name == other.name and self.allergen == other.allergen

