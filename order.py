class Order:
    def __init__(self, customer, checkout):
        self.checkout = checkout
        self.customer = customer
        self.total_cost = self.calculate_cost()
        self.completed = False

    # getters

    # returns the customer (customer)
    def get_customer(self):
        return self.customer

    # calculate cost and return cost

    def calculate_cost(self):
        for i in range(self.checkout.size):
            dish = self.checkout[i]
            self.total_cost += dish.get_price()
        return self.total_cost

    # complete the order

    def complete(self):
        self.completed = True
