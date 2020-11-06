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

    def check_order(self, order):
        for dish in order:
            if dish.name not in self.menu_str:
                return -1
        return 0

    def take_order(self, name, number, order):
        if self.check_order(order) == -1:
            return -1
        else:
            customer = c.Customer(name, number, order)
            self.add_customer(customer)
        return 0

    def add_to_order(self, customer, order):
        if customer not in self.customer_line_up or self.check_order(order) == -1:
            return -1
        else:
            index = self.customer_line_up.index(customer)
            (self.customer_line_up[index]).add_to_order(order)
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
