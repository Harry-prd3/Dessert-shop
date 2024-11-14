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

