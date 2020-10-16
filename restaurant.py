from queue import PriorityQueue

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.order_line_up = PriorityQueue
        self.money_made = 0.0
        self.customers = []

    def get_menu(self):
        return self.menu

    def get_customers(self):
        return self.customers

    def get_money_made(self):
        return self.money_made

    def get_order_line_up(self):
        return self.order_line_up

    #add_customer(Customer)

    def add_customer(self, customer):
        self.customers.append(customer)
        self.order_line_up.put(customer.get_precedence, customer.get_order())


    def find_precendence(self, customer):
        return customer.get_precedence()



