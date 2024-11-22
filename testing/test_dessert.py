from dessert import(
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_Candy():
    assert Candy("lollypop", 2, 30)
    assert Candy("taffy", 8, 40)
    assert Candy("chocolate almond", 1, 80)

def test_Cookie():
    assert Cookie("sugar", 1, 12)
    assert Cookie("pumpkin", 9, 24)
    assert Cookie("coconut", 6, 36)

def test_IceCream():
    assert IceCream("vanilla", 1, 2)
    assert IceCream("chocolate", 5, 2)
    assert IceCream("strawberry", 3, 3)

def test_Sundae():
    assert Sundae("vanilla", 1, 2, "sprinkels", 1)
    assert Sundae("chocolate", 5, 2, "chocolate chips", 2)
    assert Sundae("strawberry", 3, 3, "chocolate sauce", 1)

def test_tax():
    instance =  Candy("lollypop", 2, 30)
    assert instance.tax_percent == 7.25

def test_candy_cost():
    instance = Candy("lollypop", 2, 30)
    assert instance.calculate_cost() == 60

def test_cookie_cost():
    instance = Cookie("pumpkin", 12, 24)
    assert instance.calculate_cost() == 24

def test_icecream_cost():
    instance = IceCream("vanilla", 1, 2)
    assert instance.calculate_cost() == 2

def test_sundae_cost():
    instance = Sundae("vanilla", 1, 2, "sprinkels", 1)
    assert instance.calculate_cost() == 3

def test_super():
    assert Candy("Candy Corn", 1.5, .25).cacluate_tax() == 
    assert Candy("Gummy Bears", .25, .35)
    assert Cookie("Chocolate Chip", 6, 3.99)
    assert IceCream("Pistachio", 2, .79)
    assert Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert Cookie("Oatmeal Raisin", 2, 3.45)
    
