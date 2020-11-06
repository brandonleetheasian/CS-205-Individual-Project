import order


class Customer:
    def __init__(self, name, phone_number, order_c):
        self.name = name
        self.phone_number = phone_number
        self.served = False
        self.order = order_c

# Getters
    def get_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number

    def get_served (self):
        return self.served

    def get_order(self):
        return self.order

    # add_t0_order --> accepts dish objects
    # remove from order --> accepts dish objects
    # served

    def add_to_order(self, order_dish):
        self.order.checkout.append(order_dish)

    # checks if dish is already in order, if not returns -1
    def remove_from_order(self, order_dish):
        if order_dish not in self.order.checkout:
            return -1
        else:
            self.order.checkout.remove(order_dish)
            return 0

    def served(self):
        self.served = True

    def to_string(self):
        str_served = "Waiting to be Served"
        if self.served:
            "Already Served"
        s = self.name + ', ' + str_served
        return s

    def __eq__(self, other):
        return self.name == other.name and self.phone_number == other.phone_number

