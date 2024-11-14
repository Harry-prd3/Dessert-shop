#superclass
class DessertItem():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return(f"the name of this item is: {self.name}")
    
class Candy(DessertItem):
    def __init__(self, name, weight, price_per_pound):
        super().__init__(name)
        self.cand_weight = weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

class order():
    def __init__ (self):
        order = []
        self.order = order

    def add_Item(self, item):
        item = [item]
        self.order += item
    
    def __len__(self):
        count = 0
        for i in self.order:
            count +=1
        return count

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