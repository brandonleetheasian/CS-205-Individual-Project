import unittest
import ingredient
import customer
import dish
import order
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

        cls.dish1 = dish.Dish('French Fries', 1, cls.dish1_ingredients, 5.00, [])
        cls.dish2 = dish.Dish('Chicken Nuggets', 2, cls.dish2_ingredients, 6.00, [])
        cls.dish3 = dish.Dish('Hamburger', 3, cls.dish3_ingredients, 8.00, [])

        menu = [cls.dish1, cls.dish2, cls.dish3]

        cls.restaurant = restaurant.Restaurant(menu)

        cls.john_order = order.Order([cls.dish1, cls.dish3])
        cls.jane_order = order.Order([cls.dish2, cls.dish3])

        cls.john = customer.Customer("John", "802-888-8888", cls.john_order)
        cls.jane = customer.Customer("Jane", "802-777-7777", cls.jane_order)

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
    def test_find_precedence(self):

        print('test_add_customer()')
        # find precedence of john, should return 1 (as John was added first)
        rc = self.restaurant.find_precedence(self.john)
        self.assertEqual(rc, 1)

        # find precedence of Jane, should return 2 (as Jane was added second)
        rc = self.restaurant.find_precedence(self.jane)
        self.assertEqual(rc, 2)

        # try on customer not in restaurant, should return -1
        fake_customer = customer.Customer("Rob", "123-456-789", [])
        rc = self.restaurant.find_precedence(fake_customer)
        self.assertEqual(rc, -1)

        # remove john, and then check if john precedence (should be -1)
        self.restaurant.completed_recent_order()
        rc = self.restaurant.find_precedence(self.john)
        self.assertEqual(rc, -1)

        # with john served, jane should now be precedence 1, check if this is so
        rc = self.restaurant.find_precedence(self.jane)
        self.assertEqual(rc, 1)

    # # -------------------------------------------------------------
    # def test_check_order(self):
    #     # checks if order
    #     self.restaurant.check_order()

    # -------------------------------------------------------------
    def test_check_order_nums(self):
        order_nums = []
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, -1)

        order_nums = [1, 2, 3]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, 0)

        order_nums = [1]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, 0)

        order_nums = [2]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, 0)

        order_nums = [3]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, 0)

        order_nums = [2, 3]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, 0)

        order_nums = [5]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, -1)

        order_nums = [1, 4]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, -1)

        order_nums = [4, 5]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, -1)

        order_nums = [6, 1]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, -1)

        order_nums = [1, 1, 2, 3, 3]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, 0)

        order_nums = [1, 1, 2, 3, 4]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, -1)

        order_nums = [4, 4]
        returnVal = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(returnVal, -1)


    def test_order_nums_to_order(self):
        order_nums = [1]
        dish_list = [self.dish1]
        actual_order = order.Order(dish_list)
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [2]
        dish_list = [self.dish2]
        actual_order = order.Order(dish_list)
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [3]
        dish_list = [self.dish3]
        actual_order = order.Order(dish_list)
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [1, 2]
        dish_list = [self.dish1, self.dish2]
        actual_order = order.Order(dish_list)
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [1, 1]
        dish_list = [self.dish1, self.dish1]
        actual_order = order.Order(dish_list)
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        invalid_order = order.Order([])

        order_nums = [6]
        actual_order = invalid_order
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [6, 5]
        actual_order = order.Order([])
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = []
        actual_order = order.Order([])
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [1, 5]
        actual_order = order.Order([])
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [2, 3, 3, 5]
        actual_order = order.Order([])
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)

        order_nums = [5, 1]
        actual_order = order.Order([])
        returned_order = self.restaurant.order_nums_to_order(order_nums)
        self.assertEqual(actual_order, returned_order)


    def test_take_order(self):
        # should return -1
        test_order = self.restaurant.take_order('clay', '1234567890', [6])
        self.assertEqual(test_order, -1)
        # should return 0
        test_order = self.restaurant.take_order('brandon', '9876543210', [2])
        self.assertEqual(test_order, 0)

        test_order = self.restaurant.take_order('brandon', '9876543210', [1, 2, 3])
        self.assertEqual(test_order, 0)

        test_order = self.restaurant.take_order('clay', '7777777777', [])
        self.assertEqual(test_order, -1)








