from abc import ABC, abstractmethod
from receipt import *


#superclass
class DessertItem(ABC):
    def __init__(self, name, tax_percent = 7.25):
        self.name = name
        self.tax_percent = tax_percent
    
    def __str__(self):
        return(f"the name of this item is: {self.name}")

    @abstractmethod
    def calculate_cost():
        pass
    
    def cacluate_tax(self):
        cost = self.calculate_cost()
        tax_rate = self.tax_percent/100
        return round((cost * tax_rate),2)
    
class Candy(DessertItem):
    def __init__(self, name, weight, price_per_pound):
        super().__init__(name)
        self.cand_weight = weight
        self.price_per_pound = price_per_pound
    
    def calculate_cost(self):
        cost = self.cand_weight * self.price_per_pound
        return round(cost,2)

class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen
    
    def calculate_cost(self):
        dosnons = self.quantity/12
        cost = dosnons * self.price_per_dozen
        return round(cost,2)

class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return round(cost,2)

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    
    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price
