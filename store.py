class Store:
    def __init__(self,name):
        self.name = name
        self.products = {}
        self.new_id=0
    def add_product(self,new_product):
        self.products[self.new_id]=new_product
        print(f"Added {new_product.name} to inventory with id of {self.new_id}")
        self.new_id+=1
    def sell_product(self,id,units_sold=1):
        if id in self.products:
            if units_sold>=1:
                if self.products[id].quantity >= units_sold:
                    self.products[id].quantity -= units_sold
                else:
                    print(f"Can't sell {units_sold} {self.products[id].name}(s).")
                    print(f"Only {self.products[id].quantity} in stock.")
            else:
                print(f"You have to sell at least one {self.products[id].name}")
        else:
            print(f"Couldn't find item with id {id}")
    def inflation(self,percent_increase):
        for product in self.products.values():
            product.change_price(percent_increase,True)
    def clearance(self,percent_decrease,category):
        for product in self.products.values():
            if product.category == category:
                product.change_price(percent_decrease,False)
    def take_inventory(self):
        for id,product in self.products.items():
            print(f"Id : {id},  {product.get_quantity()} cost : {product.price}")