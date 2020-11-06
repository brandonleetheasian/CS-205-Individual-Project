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
        cls.dish3 = dish.Dish('Hamburger', 3, cls.dish3_allergens, cls.dish3_ingredients, 8.00, [])

        menu = [cls.dish1, cls.dish2, cls.dish3]

        cls.restaurant = restaurant.Restaurant(menu)

        cls.john = customer.Customer("John", "802-888-8888", [])
        cls.jane = customer.Customer("John", "802-777-7777", [])

        cls.restaurant.add_customer(cls.john)
        cls.restaurant.add_customer(cls.jane)


    @classmethod
    def tearDownClass(cls):
        # called one time, at end
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')

    def tearDown(self):
        # called after every test
        print('tearDown()')

    # -------------------------------------------------------------
    def test_(self):
        print('test_return()')
        # return john's book--should return True
        rc = self.library.return_book(self.john, self.book1)
        self.assertTrue(rc)

        # try to return the same book again--should return False
        rc = self.library.return_book(self.john, self.book1)
        self.assertFalse(rc)

        # check that the library shows that john has no books checked out
        books = self.library.get_checkouts(self.john)
        self.assertEqual(len(books), 0)

        # check that john shows no books checked out
        # right now, this code is failing, because my code is incorrect--
        # I'm returning to the library but not to Patron
        books = self.john.get_checkouts()
        self.assertEqual(len(books), 0)
