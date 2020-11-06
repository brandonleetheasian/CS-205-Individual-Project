import unittest
import ingredient
import customer
import dish
import restaurant


class TestOrder(unittest.TestCase):
    restaurant = None

    @classmethod
    def setUpClass(cls):
        # called one time, at beginning
        print('setUpClass()')
        cls.ingredient1_dish1 = ingredient.Ingredient('Potato', False)
        cls.ingredient2_dish1 = ingredient.Ingredient('Canola Oil', False)
        cls.ingredient3_dish1 = ingredient.Ingredient('Salt', False)

        cls.ingredient1_dish2 = ingredient.Ingredient('Chicken', False)
        cls.ingredient2_dish2 = ingredient.Ingredient('Flour', True)
        cls.ingredient3_dish2 = ingredient.Ingredient('Bread Crumbs', True)
        cls.ingredient4_dish2 = ingredient.Ingredient('Egg', True)
        cls.ingredient5_dish2 = ingredient.Ingredient('Salt', False)

        cls.ingredient1_dish3 = ingredient.Ingredient('Wheat Bun', True)
        cls.ingredient2_dish3 = ingredient.Ingredient('Beef', False)
        cls.ingredient3_dish3 = ingredient.Ingredient('Ketchup', False)
        cls.ingredient4_dish3 = ingredient.Ingredient('Onions', False)
        cls.ingredient5_dish3 = ingredient.Ingredient('Pickles', False)

        cls.dish1_ingredients = [cls.ingredient1_dish1, cls.ingredient2_dish1, cls.ingredient3_dish1]
        cls.dish2_ingredients = [cls.ingredient1_dish2, cls.ingredient2_dish2, cls.ingredient3_dish2, cls.ingredient4_dish2, cls.ingredient5_dish2]
        cls.dish3_ingredients = [cls.ingredient1_dish3, cls.ingredient2_dish3, cls.ingredient3_dish3, cls.ingredient4_dish3, cls.ingredient5_dish3]

        cls.dish1_allergens = []
        cls.dish2_allergens = [cls.ingredient2_dish2, cls.ingredient3_dish2, cls.ingredient4_dish2]
        cls.dish3_allergens = [cls.ingredient1_dish3]

        cls.dish1 = dish.Dish('French Fries', 1, cls.dish1_allergens, cls.dish1_ingredients, 5.00, [])
        cls.dish2 = dish.Dish('Chicken Nuggets', 2, cls.dish2_allergens, cls.dish2_ingredients, 6.00, [])
        cls.dish1 = dish.Dish('Hamburger', 3, cls.dish3_allergens, cls.dish3_ingredients, 8.00, [])

        menu = [cls.dish1, cls.dish2, cls.dish3]

        cls.restaurant(menu)


