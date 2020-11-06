import customer as c
import dish
import order


class Restaurant:

    def __init__(self, menu):
        self.menu = menu
        self.money_made = 0.0
        self.customer_line_up = []
        self.completed_orders = []
        self.menu_str = []
        for dish in self.menu:
            self.menu_str.append(dish.get_name())

    # get_menu
    # returns the menu
    def get_menu(self):
        return self.menu

    # get_customer_line_up
    # returns the customer line up list
    def get_customer_line_up(self):
        return self.customer_line_up

    # get_money_made
    # returns money made double
    def get_money_made(self):
        return self.money_made

    # add_customer
    # adds a customer to the line list
    def add_customer(self, customer):
        self.customer_line_up.append(customer)

    # find_precedence
    # finds the precedence of a customer in the line
    # if not found, the function will return -1
    def find_precedence(self, customer):
        if customer not in self.customer_line_up:
            return -1
        else:
            precedence = self.customer_line_up.index(customer) + 1
            return precedence

    # check_order
    # for every dish in the order, if the dish is not in the menu return -1
    # else return 0
    def check_order(self, order_object):
        for dish_order in order_object:
            if dish_order.dish.name not in self.menu_str:
                return -1
        return 0

    # take_order
    # adds the customers order
    def take_order(self, name, number, order_object):
        if self.check_order(order_object) == -1:
            return -1
        else:
            customer = c.Customer(name, number, order)
            self.add_customer(customer)
        return 0

    # add_to_order
    # if the customer is not in the line up return -1
    # else add the dish to the order
    def add_to_order(self, customer, order):
        if customer not in self.customer_line_up or self.check_order(order) == -1:
            return -1
        else:
            index = self.customer_line_up.index(customer)
            (self.customer_line_up[index]).add_to_order(order)
            return 0

    # cancel_order
    # if the order is found, cancel the order and return 0
    # else return -1 for customer not found
    def cancel_order(self, customer):
        if customer not in self.customer_line_up:
            return -1
        else:
            self.customer_line_up.remove(self.customer_line_up.index(customer))
            return 0

    # completed_recent_order
    # if the customer line up is empty return -1
    # else
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
