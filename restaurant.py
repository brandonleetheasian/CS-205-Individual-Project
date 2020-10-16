import dish

class Restaurant:
    def __init__(self, menu, customers, money_made, order_line_up):
        self.menu = menu
        self.customers = customers
        self.money_made = money_made
        self.order_line_up = order_line_up

    def get_menu(self):
        return self.menu

    def get_customers(self):
        return self.customers

    def get_money_made(self):
        return self.money_made

    def get_order_line_up(self):
        return self.order_line_up

    #add_customer(Customer)
    #