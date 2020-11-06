class Order:
    def __init__(self, customer, checkout):
        self.checkout = checkout
        self.total_cost = self.calculate_cost()
        self.completed = False

    # getters
    # calculate cost and return cost

    def calculate_cost(self):
        if len(self.checkout) == 0:
            return 0
        else:
            for i in range(self.checkout.size):
                dish = self.checkout[i]
                self.total_cost += dish.get_price()
            return self.total_cost

    # complete the order

    def complete(self):
        self.completed = True

    def to_string(self):
        s = ''
        for dish in self.checkout:
            s = s + str(dish) + ', '
        if len(s) == 0:
            s = 'no orders yet'
        else:
            s = s[:-2]
            s = s + ' = > ' + '$' + str(self.total_cost)
        return s
