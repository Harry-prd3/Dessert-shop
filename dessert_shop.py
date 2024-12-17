
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
        total = 0
        for item in self.order:
            total += item.cacluate_tax()
            
        return round(total,2)

    def __str__(self):
        count = 0
        for item in self.order:
            print(self.order[self.order.index(item)])
            count += 1
        return(f"you have {count} item(s) in your order.")
    

class DessertShop:
    def __init__(self):
        pass

    def user_prompt_candy(self):
        typ = False
        weight = False
        price = False
        while True:
            try:
                typ = input("what type of candy?: ")
                type(typ) == str
                break
            except ValueError:
                pass
        while True:
            try:
                weight = float(input("what is the weight of the candy?(decimal): "))
                type(weight) == float
                break
            except ValueError:
                pass
        while True:
            try:
                price = float(input("what is the the price per pound?(decimal): "))
                type(price) == float
                break
            except ValueError:
                pass

        user_candy = Candy(typ, weight, price)
        return user_candy

    def user_prompt_cookie(self):
        typ = False
        qunt = False
        price = False
        while True:
            try:
                typ = input("what type of cookie?: ")
                type(typ) == str
                break
            except ValueError:
                pass
        while True:
            try:
                qunt = input("how many cookies(number)?: ")
                type(qunt) == float
                break
            except ValueError:
                pass
        while True:
            try:
                price =  float(input("what is the the price per dozen?(decimal): "))
                type(price) == float
                break
            except ValueError:
                pass
        user_cookie = Cookie(typ, qunt, price)
        return user_cookie

    def user_prompt_icecream(self):
        typ = False
        scoops = False
        price = False
        while True:
            try:
                typ = input("what type of ice creame?: ")
                type(typ) == str
                break
            except ValueError:
                pass
        while True:
            try:
                scoops = int(input("how many scoops do you have?: "))
                type(scoops) == int
                break
            except ValueError:
                pass
        while True:
            try:
                price =  float(input("what is the the price per scoop?(decimal): "))
                type(price) == float
                break
            except ValueError:
                pass

        user_icecream = IceCream(typ, scoops, price)
        return user_icecream

    def user_prompt_sundae(self):
        typ = False
        scoops = False
        price = False
        top = False
        pice = False
        while True:
            try:
                typ = input("what type of ice creame?: ")
                type(typ) == str
                break
            except ValueError:
                pass
        while True:
            try:
                scoops = int(input("how many scoops do you have?: "))
                type(scoops) == int
                break
            except ValueError:
                pass
        while True:
            try:
                price =  float(input("what is the the price per scoop?(decimal): "))
                type(price) == float
                break
            except ValueError:
                pass
        while True:
            try:
                top = input("what topping do you have?: ")
                type(top) == str
                break
            except ValueError:
                pass
        while True:
            try:
                pice = float(input("what is the topping price?(decimal): "))
                type(pice) == float
                break
            except ValueError:
                pass

        user_sundae = Sundae(typ, scoops, price,top,pice)
        return user_sundae




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
        DATA.append([item.name, "$" + str((item.calculate_cost())), "$" + str((item.cacluate_tax()))])
    DATA.append(["subtotal", "$"+ str((defaultOrder.order_cost())), "$"+ str((defaultOrder.order_tax()))])
    DATA.append(["Total", "", "$"+ str((defaultOrder.order_cost() + defaultOrder.order_tax()))])
    DATA.append(["Total items in order", "", str(defaultOrder.__len__())])

    make_recipt(DATA, "recipt.pdf")


    shop = DessertShop()

    # boolean done = false
    done: bool = True
    # build the prompt string once
    prompt = '\n'.join([ '\n',
    '1: Candy',
    '2: Cookie',
    '3: Ice Cream',
    '4: Sunday',
    '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])
    while done:
        choice = input(prompt)
        if choice ==  '':
                done = False
        elif choice == '1':
            item = shop.user_prompt_candy()
            defaultOrder.add_Item(item)
            print(f'{item.name} has been added to your order.')
        elif choice == '2':
            item = shop.user_prompt_cookie()
            defaultOrder.add_Item(item)
            print(f'{item.name} has been added to your order.')
        elif choice == '3':
            item = shop.user_prompt_icecream()
            defaultOrder.add_Item(item)
            print(f'{item.name} has been added to your order.')
        elif '4':
            item = shop.user_prompt_sundae()
            defaultOrder.add_Item(item)
            print(f'{item.name} has been added to your order.')
        else:
            print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()
        


#runner
main()