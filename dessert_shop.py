
from receipt import *
from dessert import *

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
        for Dessertitem in order.__len__():
            total = 0
            total =+ DessertItem.cacluate_tax(order)
        return total

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

    DATA = [ 
	[ "Name", "Price", "Tax" ] 
    ] 

    for item in defaultOrder.order:
        DATA.append([item.name, "$" + str((item.calculate_cost)), "$" + str((item.cacluate_tax))])
    DATA.append(["subtotal", "$"+ str((defaultOrder.order_cost())), "$"+ str((defaultOrder.order_tax()))])
    DATA.append(["Total", "", "$"+ str((defaultOrder.order_cost() + defaultOrder.order_tax()))])
    DATA.append("Total items in order", "", str(defaultOrder.__len__()))

    make_recipt(DATA, "recipt.pdf")




#runner
main()