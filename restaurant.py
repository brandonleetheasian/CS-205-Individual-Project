import customer as c
import dish
import order
import ingredient
import copy


class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.money_made = 0.0
        self.customer_line_up = []
        self.completed_orders = []
        self.menu_str = []
        self.menu_nums = []
        for r_dish in self.menu:
            self.menu_str.append(r_dish.get_name())
            self.menu_nums.append(r_dish.get_menu_number())

    # getters

    # get menu

    def get_menu(self):
        return self.menu

    # get customer line up

    def get_customer_line_up(self):
        return self.customer_line_up

    # get money made

    def get_money_made(self):
        return self.money_made

    # get completed orders

    def get_completed_orders(self):
        return self.completed_orders

    # add customer

    def add_customer(self, customer):
        self.customer_line_up.append(customer)

    # find precedence

    def find_precedence(self, customer):
        if customer not in self.customer_line_up:
            return -1
        else:
            precedence = self.customer_line_up.index(customer) + 1
            return precedence

    # checks if array of menu numbers user wants are valid (in the menu)
    def check_order_nums(self, order_nums):
        if len(order_nums) == 0:
            return -1
        for nums in order_nums:
            if nums not in self.menu_nums:
                return -1
        return 0

    # converts array of order numbers to order objects
    def order_nums_to_order(self, order_nums):
        if self.check_order_nums(order_nums) == -1:
            invalid = order.Order([])
            return invalid
        checkout = []
        for num in order_nums:
            index = self.menu_nums.index(num)
            checkout.append(self.menu[index])
        c_order = order.Order(checkout)
        return c_order

    def order_nums_to_dish(self, order_num):
        if self.check_order_nums([order_num]) == -1:
            invalid = dish.Dish("Invalid", -1, [], -1, [])
            return invalid
        index = self.menu_nums.index(order_num)
        c_dish = self.menu[index]
        return c_dish

    # takes in name, phone number, and an array of order numbers, and adds the customer to customer line
    def take_order(self, name, number, order_nums):
        if self.check_order_nums(order_nums) == -1:
            return -1
        else:
            c_order = self.order_nums_to_order(order_nums)
            customer = c.Customer(name, number, c_order)
            self.add_customer(customer)
        return 0

    def add_to_order(self, customer, order_nums):
        if customer not in self.customer_line_up or self.check_order_nums(order_nums) == -1:
            return -1
        else:
            c_order = copy.deepcopy(self.order_nums_to_order(order_nums))
            index = self.customer_line_up.index(customer)
            customer_c = (self.customer_line_up[index])
            customer_c.add_to_order(c_order)
            return 0

    def cancel_order(self, customer):
        if customer not in self.customer_line_up:
            return -1
        else:
            self.customer_line_up.remove(customer)
            return 0

    def completed_recent_order(self):
        if len(self.customer_line_up) == 0:
            return -1
        else:
            customer_c = self.customer_line_up.pop(0)
            # customer_c.served()
            # customer_c.order.completed()
            order_finished = customer_c.get_order()
            self.money_made += order_finished.calculate_cost()
            self.completed_orders.append(customer_c)
            return 0

    def list_allergens(self, order_num):
        return_val = self.check_order_nums([order_num])
        if return_val == -1:
            invalid = ingredient.Ingredient("invalid", False)
            invalid_list = [invalid]
            return invalid_list
        else:
            c_dish = self.order_nums_to_dish(order_num)
            allergens = c_dish.get_allergens()
            return allergens

    # list_ingredients method that returns the ingredients of a given dish

    def list_ingredients(self, dish_num):
        invalid = []
        validation = self.check_order_nums([dish_num])
        # put into array to check if dish num is valid
        if validation == 0:
            # convert to dish
            temp_dish = self.order_nums_to_dish(dish_num)
            # return dish ingredient
            return temp_dish.get_ingredients()
        # else
        else:
            return invalid

    # add_unwanted_ingredients that returns -1 or 0 and removes an unwanted ingredient from the ingredients in a
    # particular dish and adds it to unwanted ingredients in a particular order --> see similar method in dish
    # NOTE: should take in an ingredient, an order, and a dish --> make sure that the order is valid,
    # the dish in the order, and then if the ingredient is in the dish. If all are true,
    # Do the operation and return 0. Else, return -1

    def add_unwanted_ingredients(self, unwanted_ingredient, customer, dish_num):
        if customer not in self.customer_line_up or self.check_order_nums([dish_num]) == -1 or unwanted_ingredient not in self.order_nums_to_dish(dish_num).get_ingredients():
            return -1
        else:
            # find index of customer in lineup
            index = self.customer_line_up.index(customer)
            # get order
            c_order = self.customer_line_up[index].get_order()
            # get dishes from order
            dish_list = c_order.get_checkout()
            c_dish = self.order_nums_to_dish(dish_num)
            # if the given dish object is in the list of dishes from the order
            if c_dish in dish_list:
            # find the indices/index of dish
                indices = [i for i, x in enumerate(dish_list) if x == c_dish]
                for i in indices:
                    dish_list[i].add_unwanted_ingredients(unwanted_ingredient)
            return 0




    # remove unwanted ingredients that returns -1 of 0 and removes an unwanted ingredient from the unwanted
    # ingredients list and reads it back into ingredients for a particular dish in a particular
    # order --> see similar method in dish
    #  NOTE: should take in an ingredient, an order, and a dish --> make sure that the order is
    #  valid, the dish in the order, and then if the ingredient is in unwanted list in the dish.
    #  If all are true, Do the operation and return 0. Else, return -1

    def remove_unwanted_ingredient(self, unwanted_ingredient, customer, dish_num):

        if customer not in self.customer_line_up or self.check_order_nums([dish_num]) == -1 or unwanted_ingredient not in self.order_nums_to_dish(dish_num).get_ingredients():
            return -1
        else:
            # find index of customer in lineup
            index = self.customer_line_up.index(customer)
            # get order
            c_order = self.customer_line_up[index].get_order()
            # get dishes from order
            dish_list = c_order.get_checkout()
            c_dish = self.order_nums_to_dish(dish_num)
            # if the given dish object is in the list of dishes from the order
            if c_dish in dish_list:
            # find the indices/index of dish
                indices = [i for i, x in enumerate(dish_list) if x == c_dish]
                for i in indices:
                    dish_list[i].remove_unwanted_ingredients(unwanted_ingredient)
            return 0
