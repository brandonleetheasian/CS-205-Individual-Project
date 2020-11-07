import order


class Customer:
    def __init__(self, name, phone_number, order_c):
        self.name = name
        self.phone_number = phone_number
        self.order = order_c

# Getters
    def get_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number

    def get_order(self):
        return self.order

    # add_t0_order --> accepts dish objects
    # remove from order --> accepts dish objects
    # served

    def add_to_order(self, order_c):
        self.order.checkout.extend(order_c.checkout)

    # checks if dish is already in order, if not returns -1
    def remove_from_order(self, order_dish):
        if order_dish not in self.order.checkout:
            return -1
        else:
            self.order.checkout.remove(order_dish)
            return 0

    def to_string(self):
        s = self.name + ', ' + self.phone_number
        return s

    def __eq__(self, other):
        return self.name == other.name and self.phone_number == other.phone_number

