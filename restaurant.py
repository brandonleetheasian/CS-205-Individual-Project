from customer import Customer


class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.money_made = 0.0
        self.customer_line_up = []
        self.completed_orders = []

    def get_menu(self):
        return self.menu

    def get_customer_line_up(self):
        return self.customer_line_up

    def get_money_made(self):
        return self.money_made

    def add_customer(self, customer):
        self.customer_line_up.append(customer)

    def find_precedence(self, customer):
        precedence = self.customer_line_up.index(customer) + 1
        return precedence

    def take_order(self, name, number, order):
        customer = Customer(name, number, order)
        self.customer_line_up.append(customer)

    def cancel_order(self, customer):
        self.customer_line_up.remove(self.customer_line_up.index(customer))

    def completed_recent_order(self):
        customer = self.customer_line_up.pop(0)
        order_finished = customer.get_order()
        self.money_made += order_finished.calculate_cost
        self.completed_orders.append(customer)
