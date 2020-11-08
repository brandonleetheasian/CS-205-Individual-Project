import unittest
import ingredient
import customer
import dish
import order
import restaurant
import copy


class TestOrder(unittest.TestCase):

    restaurant = None

    @classmethod
    def setUpClass(cls):
        # called one time, at beginning
        print('setUpClass()')
        # cls.ingredient1_dish1 = ingredient.Ingredient('Potato', False)
        # cls.ingredient2_dish1 = ingredient.Ingredient('Canola Oil', False)
        # cls.ingredient3_dish1 = ingredient.Ingredient('Salt', False)
        #
        # cls.ingredient1_dish2 = ingredient.Ingredient('Chicken', False)
        # cls.ingredient2_dish2 = ingredient.Ingredient('Flour', True)
        # cls.ingredient3_dish2 = ingredient.Ingredient('Bread Crumbs', True)
        # cls.ingredient4_dish2 = ingredient.Ingredient('Egg', True)
        # cls.ingredient5_dish2 = ingredient.Ingredient('Salt', False)
        #
        # cls.ingredient1_dish3 = ingredient.Ingredient('Wheat Bun', True)
        # cls.ingredient2_dish3 = ingredient.Ingredient('Beef', False)
        # cls.ingredient3_dish3 = ingredient.Ingredient('Ketchup', False)
        # cls.ingredient4_dish3 = ingredient.Ingredient('Onions', False)
        # cls.ingredient5_dish3 = ingredient.Ingredient('Pickles', False)
        #
        # cls.dish1_ingredients = [cls.ingredient1_dish1, cls.ingredient2_dish1, cls.ingredient3_dish1]
        # cls.dish2_ingredients = [cls.ingredient1_dish2, cls.ingredient2_dish2, cls.ingredient3_dish2, cls.ingredient4_dish2, cls.ingredient5_dish2]
        # cls.dish3_ingredients = [cls.ingredient1_dish3, cls.ingredient2_dish3, cls.ingredient3_dish3, cls.ingredient4_dish3, cls.ingredient5_dish3]
        #
        # cls.dish1 = dish.Dish('French Fries', 1, cls.dish1_ingredients, 5.00, [])
        # cls.dish2 = dish.Dish('Chicken Nuggets', 2, cls.dish2_ingredients, 6.00, [])
        # cls.dish3 = dish.Dish('Hamburger', 3, cls.dish3_ingredients, 8.00, [])
        #
        # cls.menu = [cls.dish1, cls.dish2, cls.dish3]
        #
        # cls.restaurant = restaurant.Restaurant(cls.menu)
        #
        # cls.john_order = order.Order([cls.dish1, cls.dish3])
        # cls.jane_order = order.Order([cls.dish2, cls.dish3])
        #
        # cls.john = customer.Customer("John", "802-888-8888", cls.john_order)
        # cls.jane = customer.Customer("Jane", "802-777-7777", cls.jane_order)
        #
        # cls.restaurant.add_customer(cls.john)
        # cls.restaurant.add_customer(cls.jane)


    @classmethod
    def tearDownClass(cls):
        # called one time, at end
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')
        self.ingredient1_dish1 = ingredient.Ingredient('Potato', False)
        self.ingredient2_dish1 = ingredient.Ingredient('Canola Oil', False)
        self.ingredient3_dish1 = ingredient.Ingredient('Salt', False)

        self.ingredient1_dish2 = ingredient.Ingredient('Chicken', False)
        self.ingredient2_dish2 = ingredient.Ingredient('Flour', True)
        self.ingredient3_dish2 = ingredient.Ingredient('Bread Crumbs', True)
        self.ingredient4_dish2 = ingredient.Ingredient('Egg', True)
        self.ingredient5_dish2 = ingredient.Ingredient('Salt', False)

        self.ingredient1_dish3 = ingredient.Ingredient('Wheat Bun', True)
        self.ingredient2_dish3 = ingredient.Ingredient('Beef', False)
        self.ingredient3_dish3 = ingredient.Ingredient('Ketchup', False)
        self.ingredient4_dish3 = ingredient.Ingredient('Onions', False)
        self.ingredient5_dish3 = ingredient.Ingredient('Pickles', False)

        self.dish1_ingredients = [self.ingredient1_dish1, self.ingredient2_dish1, self.ingredient3_dish1]
        self.dish2_ingredients = [self.ingredient1_dish2, self.ingredient2_dish2, self.ingredient3_dish2, self.ingredient4_dish2, self.ingredient5_dish2]
        self.dish3_ingredients = [self.ingredient1_dish3, self.ingredient2_dish3, self.ingredient3_dish3, self.ingredient4_dish3, self.ingredient5_dish3]

        self.dish1 = dish.Dish('French Fries', 1, self.dish1_ingredients, 5.00, [])
        self.dish2 = dish.Dish('Chicken Nuggets', 2, self.dish2_ingredients, 6.00, [])
        self.dish3 = dish.Dish('Hamburger', 3, self.dish3_ingredients, 8.00, [])

        self.menu = [self.dish1, self.dish2, self.dish3]

        self.restaurant = restaurant.Restaurant(self.menu)

        self.john_order = order.Order([copy.deepcopy(self.dish1), copy.deepcopy(self.dish3)])
        self.jane_order = order.Order([copy.deepcopy(self.dish2), copy.deepcopy(self.dish3)])

        self.john = customer.Customer("John", "802-888-8888", self.john_order)
        self.jane = customer.Customer("Jane", "802-777-7777", self.jane_order)

        self.restaurant.add_customer(self.john)
        self.restaurant.add_customer(self.jane)

    def tearDown(self):
        # called after every test
        print('tearDown()')


    # -------------------------------------------------------------
    def test_find_precedence(self):

        print('test_add_customer()')
        print(self.john in self.restaurant.get_customer_line_up())
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
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, -1)

        order_nums = [1, 2, 3]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, 0)

        order_nums = [1]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, 0)

        order_nums = [2]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, 0)

        order_nums = [3]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, 0)

        order_nums = [2, 3]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, 0)

        order_nums = [5]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, -1)

        order_nums = [1, 4]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, -1)

        order_nums = [4, 5]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, -1)

        order_nums = [6, 1]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, -1)

        order_nums = [1, 1, 2, 3, 3]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, 0)

        order_nums = [1, 1, 2, 3, 4]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, -1)

        order_nums = [4, 4]
        return_val = self.restaurant.check_order_nums(order_nums)
        self.assertEqual(return_val, -1)


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

    def test_order_nums_to_dish(self):
        order_num = 1
        actual_dish = self.dish1
        returned_dish = self.restaurant.order_nums_to_dish(order_num)
        self.assertEqual(actual_dish, returned_dish)

        order_num = 2
        actual_dish = self.dish2
        returned_dish = self.restaurant.order_nums_to_dish(order_num)
        self.assertEqual(actual_dish, returned_dish)

        order_num = 3
        actual_dish = self.dish3
        returned_dish = self.restaurant.order_nums_to_dish(order_num)
        self.assertEqual(actual_dish, returned_dish)

        order_num = 4
        actual_dish = dish.Dish("Invalid", -1, [], -1, [])
        returned_dish = self.restaurant.order_nums_to_dish(order_num)
        self.assertEqual(actual_dish, returned_dish)

        order_num = 31
        actual_dish = dish.Dish("Invalid", -1, [], -1, [])
        returned_dish = self.restaurant.order_nums_to_dish(order_num)
        self.assertEqual(actual_dish, returned_dish)

        order_num = 0
        actual_dish = dish.Dish("Invalid", -1, [], -1, [])
        returned_dish = self.restaurant.order_nums_to_dish(order_num)
        self.assertEqual(actual_dish, returned_dish)

        order_num = -1
        actual_dish = dish.Dish("Invalid", -1, [], -1, [])
        returned_dish = self.restaurant.order_nums_to_dish(order_num)
        self.assertEqual(actual_dish, returned_dish)

    def test_take_order(self):
        empty_order = order.Order([])
        # should return -1
        test_order = self.restaurant.take_order('Clay', '1234567890', [6])
        self.assertEqual(test_order, -1)
        # check if new user is in customer lineup
        clay = customer.Customer('Clay', '1234567890', empty_order)
        lineup = self.restaurant.get_customer_line_up()
        self.assertFalse(clay in lineup)

        # should return 0
        b_order = order.Order([self.dish2])
        test_order = self.restaurant.take_order('Brandon', '9876543210', [2])
        self.assertEqual(test_order, 0)
        # check if new user is in customer lineup
        brandon = customer.Customer('Brandon', '9876543210', b_order)
        lineup = self.restaurant.get_customer_line_up()
        self.assertTrue(brandon in lineup)

        n_order = order.Order([self.dish1, self.dish2, self.dish3])
        test_order = self.restaurant.take_order('Nick', '9876543210', [1, 2, 3])
        self.assertEqual(test_order, 0)
        # check if new user is in customer lineup
        nick = customer.Customer('Nick', '9876543210', b_order)
        lineup = self.restaurant.get_customer_line_up()
        self.assertTrue(nick in lineup)

        j_order = order.Order([])
        test_order = self.restaurant.take_order('Jake', '777777777', [])
        self.assertEqual(test_order, -1)
        # check if new user is in customer lineup
        jake = customer.Customer('Jake', '777777777', j_order)
        lineup = self.restaurant.get_customer_line_up()
        self.assertFalse(jake in lineup)

        s_order = order.Order([self.dish1, self.dish2])
        test_order = self.restaurant.take_order('Stephen', '4657485', [1, 2, 6])
        self.assertEqual(test_order, -1)
        # check if new user is in customer lineup
        stephen = customer.Customer('Stephen', '4657485', s_order)
        lineup = self.restaurant.get_customer_line_up()
        self.assertFalse(stephen in lineup)

    def test_add_to_order(self):

        order_c = copy.deepcopy(self.jane.get_order())
        return_val = self.restaurant.add_to_order(self.jane, [1])
        self.assertEqual(return_val, 0)
        # check if customer order changed
        index = self.restaurant.get_customer_line_up().index(self.jane)
        customer_c = (self.restaurant.get_customer_line_up())[index]
        order_c.add_dish([self.dish1])
        self.assertEqual(customer_c.get_order(), order_c)

        order_c = copy.deepcopy(self.john.get_order())
        return_val = self.restaurant.add_to_order(self.john, [1, 2])
        self.assertEqual(return_val, 0)
        # check if customer order changed
        index = self.restaurant.get_customer_line_up().index(self.john)
        customer_c = (self.restaurant.get_customer_line_up())[index]
        order_c.add_dish([self.dish1, self.dish2])
        self.assertEqual(customer_c.get_order(), order_c)

        order_c = copy.deepcopy(self.john.get_order())
        return_val = self.restaurant.add_to_order(self.john, [1, 2, 3])
        self.assertEqual(return_val, 0)
        # check if customer order changed
        index = self.restaurant.get_customer_line_up().index(self.john)
        customer_c = (self.restaurant.get_customer_line_up())[index]
        order_c.add_dish([self.dish1, self.dish2, self.dish3])
        self.assertEqual(customer_c.get_order(), order_c)

        order_c = copy.deepcopy(self.john.get_order())
        return_val = self.restaurant.add_to_order(self.john, [6])
        self.assertEqual(return_val, -1)
        # check if customer order changed
        index = self.restaurant.get_customer_line_up().index(self.john)
        customer_c = (self.restaurant.get_customer_line_up())[index]
        order_c.add_dish([])
        self.assertEqual(customer_c.get_order(), order_c)

        order_c = copy.deepcopy(self.jane.get_order())
        return_val = self.restaurant.add_to_order(self.jane, [])
        self.assertEqual(return_val, -1)
        # check if customer order changed
        index = self.restaurant.get_customer_line_up().index(self.jane)
        customer_c = (self.restaurant.get_customer_line_up())[index]
        order_c.add_dish([])
        self.assertEqual(customer_c.get_order(), order_c)

        order_c = copy.deepcopy(self.jane.get_order())
        return_val = self.restaurant.add_to_order(self.jane, [1, 6])
        self.assertEqual(return_val, -1)
        # check if customer order changed
        index = self.restaurant.get_customer_line_up().index(self.jane)
        customer_c = (self.restaurant.get_customer_line_up())[index]
        order_c.add_dish([])
        self.assertEqual(customer_c.get_order(), order_c)

        order_c = copy.deepcopy(self.jane.get_order())
        return_val = self.restaurant.add_to_order(self.jane, [4, 6])
        self.assertEqual(return_val, -1)
        # check if customer order changed
        index = self.restaurant.get_customer_line_up().index(self.jane)
        customer_c = (self.restaurant.get_customer_line_up())[index]
        order_c.add_dish([])
        self.assertEqual(customer_c.get_order(), order_c)

    def test_cancel_order(self):
        empty_order = order.Order([])

        return_val = self.restaurant.cancel_order(self.john)
        self.assertEqual(return_val, 0)
        # check if customer is still in line
        line = self.restaurant.get_customer_line_up()
        self.assertFalse(self.john in line)

        return_val = self.restaurant.cancel_order(self.jane)
        self.assertEqual(return_val, 0)
        # check if customer is still in line
        line = self.restaurant.get_customer_line_up()
        self.assertFalse(self.john in line)

        # check to see if we can remove john again, should return -1, because john is gone
        return_val = self.restaurant.cancel_order(self.john)
        self.assertEqual(return_val, -1)

        brandon = customer.Customer("Brandon", "1111111111", empty_order)
        return_val = self.restaurant.cancel_order(brandon)
        self.assertEqual(return_val, -1)
        # check if customer is still in line
        line = self.restaurant.get_customer_line_up()
        self.assertFalse(brandon in line)

        # add brandon to line and then cancel, should return 0 because valid, then checks if brandon is in line (which he shouldn't be)
        self.restaurant.add_customer(brandon)
        return_val = self.restaurant.cancel_order(brandon)
        self.assertEqual(return_val, 0)
        self.assertFalse(brandon in line)

    def test_completed_recent_order(self):
        # complete most recent order (should be john), check line if john left, check if overall price went up by john's order, and then check if john is in completed orders
        return_val = self.restaurant.completed_recent_order()
        self.assertEqual(return_val, 0)
        self.assertFalse(self.john in self.restaurant.get_customer_line_up())
        self.assertEqual(self.john.get_order().calculate_cost(), self.restaurant.get_money_made())
        self.assertTrue(self.john in self.restaurant.get_completed_orders())

        # complete most recent order (should be jane now), check line if jane left, check if overall price went yp by jane's order (should now be jane + john), and then check if jane is in completed orders
        return_val = self.restaurant.completed_recent_order()
        self.assertEqual(return_val, 0)
        self.assertFalse(self.jane in self.restaurant.get_customer_line_up())
        self.assertEqual(self.jane.get_order().calculate_cost() + self.john.get_order().calculate_cost(), self.restaurant.get_money_made())
        self.assertTrue(self.jane in self.restaurant.get_completed_orders())

        # complete most recent order (should be no one now) and returned should be -1. Check if the completed line is still as expected (a list of john and jane)
        expected_completed_list = [self.john, self.jane]
        return_val = self.restaurant.completed_recent_order()
        self.assertEqual(return_val, -1)
        self.assertEqual(expected_completed_list, self.restaurant.get_completed_orders())

    def test_list_allergens(self):
        # list a valid order number 3, should return wheat bun in a list,
        actual = self.restaurant.list_allergens(3)
        expected = [self.ingredient1_dish3]
        self.assertEqual(actual, expected)

        # list a valid order number 2, should return a list of flour, breadcrumbs, and eggs
        actual = self.restaurant.list_allergens(2)
        expected = [self.ingredient2_dish2, self.ingredient3_dish2, self.ingredient4_dish2]
        self.assertEqual(actual, expected)

        # list a valid order number 1, should return an empty list
        actual = self.restaurant.list_allergens(1)
        expected = []
        self.assertEqual(actual, expected)

        # list a invalid order number -1, should return a list with an ingredient list of invalid
        actual = self.restaurant.list_allergens(4)
        expected = [ingredient.Ingredient("invalid", False)]
        self.assertEqual(actual, expected)

        # list a invalid order number 5, should return a list with an ingredient list of invalid
        actual = self.restaurant.list_allergens(-1)
        expected = [ingredient.Ingredient("invalid", False)]
        self.assertEqual(actual, expected)

    def test_list_ingredients(self):
        # list a valid order number 1, should return a list of ingredients for french fries
        actual = self.restaurant.list_ingredients(1)
        expected = [self.ingredient1_dish1, self.ingredient2_dish1, self.ingredient3_dish1]
        self.assertEqual(actual, expected)

        # list a valid order number 2, should return a list of ingredients for chicken nuggets
        actual = self.restaurant.list_ingredients(2)
        expected = [self.ingredient1_dish2, self.ingredient2_dish2, self.ingredient3_dish2, self.ingredient4_dish2, self.ingredient5_dish2]
        self.assertEqual(actual, expected)

        # list a valid order number 1, should return a list of ingredients for hamburger
        actual = self.restaurant.list_ingredients(3)
        expected = [self.ingredient1_dish3, self.ingredient2_dish3, self.ingredient3_dish3, self.ingredient4_dish3, self.ingredient5_dish3]
        self.assertEqual(actual, expected)

        # list an invalid order number -1, should return an empty list of ingredients
        actual = self.restaurant.list_ingredients(-1)
        expected = []
        self.assertEqual(actual, expected)

        # list an invalid order number 10, should return an empty list of ingredients
        actual = self.restaurant.list_ingredients(10)
        expected = []
        self.assertEqual(actual, expected)

    def test_add_unwanted_ingredients(self):
        # validity test, give a valid customer, a valid unwanted ingredient and a valid dish, should return 0
        # check if the customer's order changed
        # first, create a copy of the ingredients of the dish
        ingredients = copy.deepcopy(self.dish1_ingredients)
        # create the unwanted ingredient
        unwanted_ingredient = ingredient.Ingredient("Salt", False)
        return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.john, 1)
        self.assertEqual(return_val, 0)
        # make it so that the unwanted ingredient is removed from the copy of ingredients
        ingredients.remove(self.ingredient3_dish1)
        # check the dishes
        expected_dish = dish.Dish("French Fries", 1, ingredients, 5.00, [unwanted_ingredient])
        # check if the expected order is good
        expected_order = order.Order([expected_dish, self.dish3])
        self.assertEqual(self.restaurant.get_customer_line_up()[0].get_order(), expected_order)

        # # validity test, give a valid customer, a valid unwanted ingredient and a valid dish, should return 0
        # # check if the customer's order changed
        # # first, create a copy of the ingredients of the dish
        # ingredients = copy.deepcopy(self.dish1_ingredients)
        # # create the unwanted ingredient
        # unwanted_ingredient = ingredient.Ingredient("Salt", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.john, 1)
        # self.assertEqual(return_val, 0)
        # # make it so that the unwanted ingredient is removed from the copy of ingredients
        # ingredients.remove(self.ingredient3_dish1)
        # # check the dishes
        # expected_dish = dish.Dish("French Fries", 1, ingredients, 5.00, [unwanted_ingredient])
        # # check if the expected order is good
        # expected_order = order.Order([expected_dish, self.dish3])
        # self.assertEqual(self.restaurant.get_customer_line_up()[0].get_order(), expected_order)
        #
        #
        # # invalidity test, give a valid customer, a valid unwanted ingredient and a valid dish,
        # # but the unwanted ingredient has already been excluded should return 0
        # # check if the customer's order changed
        # unwanted_ingredient = ingredient.Ingredient("Salt", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.john, 1)
        # self.assertEqual(return_val, 0)
        # ingredients = copy.deepcopy(self.dish1_ingredients)
        # ingredients.remove(unwanted_ingredient)
        # expected_dish = dish.Dish("French Fries", 1, ingredients, 5.00, [unwanted_ingredient])
        # expected_order = order.Order([expected_dish, self.dish3])
        # self.assertEqual(self.restaurant.get_customer_line_up()[0].get_order(), expected_order)
        #
        # # invalidity test, give a valid customer, an invalid unwanted ingredient and a valid dish, should return -1
        # # check to see if the customer's order changed (it shouldn't have)
        # unwanted_ingredient = ingredient.Ingredient("Lamb", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.john, 1)
        # self.assertEqual(return_val, -1)
        # ingredients = copy.deepcopy(self.dish1_ingredients)
        # ingredients.remove(unwanted_ingredient)
        # expected_dish = dish.Dish("French Fries", 1, ingredients, 5.00, [ingredient.Ingredient("Salt", False)])
        # expected_order = order.Order([expected_dish, self.dish3])
        # self.assertEqual(self.restaurant.get_customer_line_up()[0].get_order(), expected_order)
        #
        # # invalidity test, give a valid customer, a valid unwanted ingredient and a valid dish,
        # # but the customer does not have that dish in his/her order should return -1
        # # check to see if the customer's order changed (it shouldn't have)
        # unwanted_ingredient = ingredient.Ingredient("Salt", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.jane, 1)
        # self.assertEqual(return_val, -1)
        # expected_order = order.Order([self.dish2, self.dish3])
        # self.assertEqual(self.restaurant.get_customer_line_up()[1].get_order(), expected_order)
        #
        # # invalidity test, give a valid customer, an ingredients that exists on the menu,
        # # but an invalid dish, should return -1
        # # check to see if the customer's order changed (it shouldn't have)
        # unwanted_ingredient = ingredient.Ingredient("Salt", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.john, 5)
        # self.assertEqual(return_val, -1)
        # ingredients = copy.deepcopy(self.dish1_ingredients)
        # ingredients.remove(unwanted_ingredient)
        # expected_dish = dish.Dish("French Fries", 1, ingredients, 5.00, [ingredient.Ingredient("Salt", False)])
        # expected_order = order.Order([expected_dish, self.dish3])
        # self.assertEqual(self.restaurant.get_customer_line_up()[0].get_order(), expected_order)
        #
        #
        # # invalidity test, give a valid customer, an ingredients that exists on the menu,
        # # but a valid dish where that ingredient doesn't exist in, should return -1
        # # check to see if the customer's order changed (it shouldn't have)
        # unwanted_ingredient = ingredient.Ingredient("Salt", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.jane, 3)
        # self.assertEqual(return_val, -1)
        # expected_dish = dish.Dish("Hamburger", 3, self.dish3_ingredients, 8.00, [])
        # expected_order = order.Order([self.dish2, expected_dish])
        # self.assertEqual(self.restaurant.get_customer_line_up()[1].get_order(), expected_order)
        #
        #
        # # invalidity test, give an invalid customer, a valid unwanted ingredient, and a valid dish, should return -1
        # # this invalid customer will have this valid dish in his "order", but will not be in the line up
        # empty_order = order.Order([self.dish1])
        # clay = customer.Customer('Clay', '1234567890', empty_order)
        # unwanted_ingredient = ingredient.Ingredient("Salt", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, clay, 1)
        # self.assertEqual(return_val, -1)
        #
        # # validity test, give a different valid customer, a valid unwanted ingredient and a valid dish, should return 0
        # # check if the customer's order changed
        # unwanted_ingredient = ingredient.Ingredient("Pickles", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.jane, 3)
        # self.assertEqual(return_val, 0)
        # expected_dish = dish.Dish("Hamburger", 3, self.dish1_ingredients, 8.00, [unwanted_ingredient])
        # expected_order = order.Order([expected_dish, self.dish3])
        # self.assertEqual(self.restaurant.get_customer_line_up()[0].get_order(), expected_order)
        #
        # # validity test, give a valid customer, a valid unwanted ingredient and a valid dish, should return 0
        # # check if the customer's order changed
        # unwanted_ingredient = ingredient.Ingredient("Salt", False)
        # return_val = self.restaurant.add_unwanted_ingredients(unwanted_ingredient, self.john, 1)
        # self.assertEqual(return_val, 0)
        # expected_dish = dish.Dish("French Fries", 1, self.dish1_ingredients, 5.00, [unwanted_ingredient])
        # expected_order = order.Order([expected_dish, self.dish3])
        # self.assertEqual(self.restaurant.get_customer_line_up()[0].get_order(), expected_order)
        #
        #
        # # invalid test, give all invalid arguments, should return -1



if __name__ == "__main__":
    unittest.main()








