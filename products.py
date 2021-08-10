class Product:
    def __init__(self,name,price,catergory,quantity=0):
        self.name = name
        self.price = price
        self.category = catergory
        self.quantity = quantity
    def change_price(self,percent_changed,is_increase):
        if is_increase:
            self.price = round(self.price*(1+(percent_changed/100)),2)
        else:
            self.price = round(self.price*(1-(percent_changed/100)),2)
    def print_info(self):
        print(f"{self.name} in category {self.category} costs {self.cost}")
    def get_quantity(self):
        return(f"{self.name} - {self.quantity}")