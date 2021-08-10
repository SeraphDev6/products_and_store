from store import Store
from products import Product
m = Store("Markus' Market")
m.add_product(Product("Marcus' Mashed Mushrooms",5.99,"Food",20))
m.take_inventory()
m.sell_product(0)
m.take_inventory()
m.add_product(Product("Marcus' Marinated Mackeral",20.99,"Food",100))
m.inflation(10)
m.take_inventory()
m.clearance(5,"Food")
m.take_inventory()
m.sell_product(2)
m.take_inventory()