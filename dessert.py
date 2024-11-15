from abc import ABC, abstractmethod

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
    
    def cacluate_tax(self, cost):
        return cost * self.tax_percent
    
class Candy(DessertItem):
    def __init__(self, name, weight, price_per_pound):
        super().__init__(name)
        self.cand_weight = weight
        self.price_per_pound = price_per_pound
    
    def calculate_cost(self):
        cost = self.cand_weight * self.price_per_pound
        return cost

class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen
    
    def calculate_cost(self):
        cost = self.quantity/self.price_per_dozen
        return cost

class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return cost

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    
    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price

class order():
    def __init__ (self):
        order = []
        self.order = order

    def add_Item(self, item):
        item = [item]
        self.order += item
    
    def __len__(self):
        count = 0
        for item in self.order:
            count +=1
        return count

    def order_cost(self):
        price = 0
        for item in self.order:
            price += item.calculate_cost()
        return price
    
    def order_tax(self):
        total = DessertItem.cacluate_tax(order)

    def __str__(self):
        count = 0
        for item in self.order:
            print(self.order[self.order.index(item)])
            count += 1
        return(f"you have {count} item(s) in your order.")




def main():
    defaultOrder = order()
    defaultOrder.add_Item(Candy("Candy Corn", 1.5, .25))
    defaultOrder.add_Item(Candy("Gummy Bears", .25, .35))
    defaultOrder.add_Item(Cookie("Chocolate Chip", 6, 3.99))
    defaultOrder.add_Item(IceCream("Pistachio", 2, .79))
    defaultOrder.add_Item(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    defaultOrder.add_Item(Cookie("Oatmeal Raisin", 2, 3.45))


    
    print(defaultOrder)


#runner
main()