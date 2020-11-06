import unittest
import dish
import customer

def tester():
    mac_ingredients = ['noodles', 'cheese', 'milk', 'salt']
    mac_allergens = ['milk', 'cheese']
    mac_unwanted = []

    dish1 = dish.Dish('mac & cheese', 5, mac_allergens, mac_ingredients, 6.99, mac_unwanted)
