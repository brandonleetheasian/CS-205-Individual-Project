class Ingredient:
    def __init__(self, name, allergen):
        self.name = name
        self.allergen = allergen

    def get_name(self):
        return self.name

    def get_allergen(self):
        return self.allergen
