import dish

class Customer:
    def __init__(self, name, phone_number, order):
      self.name = name
      self.phone_number = phone_number
      self.served = False
      self.order = order


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
    def add_to_order(self, dish):


    def to_string(self):
        s = '"' + self.title + '" ' + self.author + ' ' + self.catalog_number
        return s

    def get_title(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))
