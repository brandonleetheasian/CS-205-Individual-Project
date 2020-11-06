import customer as c
import dish
import order
import ingredient


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

    def get_menu(self):
        return self.menu

    def get_customer_line_up(self):
        return self.customer_line_up

    def get_money_made(self):
        return self.money_made

    def add_customer(self, customer):
        self.customer_line_up.append(customer)

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

    # def check_order_num(self, order_num):
    #     if order_num not in self.menu_nums:
    #         return -1
    #     else:
    #         return 0

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
            c_order = self.order_nums_to_order(order_nums)
            index = self.customer_line_up.index(customer)
            (self.customer_line_up[index]).add_to_order(c_order)
            return 0


    def cancel_order(self, customer):
        if customer not in self.customer_line_up:
            return -1
        else:
            self.customer_line_up.remove(self.customer_line_up.index(customer))
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
            return invalid
        else:
            c_dish = self.order_nums_to_order([order_num])[0]
            allergens = c_dish.get_allergens()
            return allergens

    #list_ingredients method that returns the ingredients of a given dish

    #add_unwanted_ingredients that returns -1 or 0 and removes an unwanted ingredient from the ingredients in a particular dish and adds it to unwanted ingredients in a particular order --> see similar method in dish
    #NOTE: should take in an ingredient, an order, and a dish --> make sure that the order is valid, the dish in the order, and then if the ingredient is in the dish. If all are true, Do the operation and return 0. Else, return -1

    #remove unwanted ingredients that returns -1 of 0 and removes an unwanted ingredient from the unwanted ingredients list and readds it back into ingredients for a partular dish in a particulay order --> see similar method in dish
    # NOTE: should take in an ingredient, an order, and a dish --> make sure that the order is valid, the dish in the order, and then if the ingredient is in unwanted list in the dish. If all are true, Do the operation and return 0. Else, return -1