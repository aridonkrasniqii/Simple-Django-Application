from item import Item

item1 = Item("MyItem", 100, 1)
# item1.name = "akldaslkdhasdasdk`"
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)
