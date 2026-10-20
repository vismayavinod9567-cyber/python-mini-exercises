# food delivery system using oop in python 

class restaurant:
    def __init__(self,rest_id,rest_name,location):
        self.rest_id=rest_id
        self.rest_name=rest_name
        self.location=location

    def restaurant_info(self):
        print(f"restuarant inforation :\nrestaurant id:{self.rest_id}\nrestaurant name:{self.rest_name}\nlocation:{self.location}")
class customwer:
    def __init__(self,cust_id,cust_name,address):
        self.cust_id=cust_id
        self.cust_name=cust_name
        self.address=address
    def customer_info(self):
        print(f"customer detaila:\ncustomer ID:{self.cust_id}\ncustomer name:{self.cust_name}\naddress:{self.address}")
class order:
    def __init__(self,order_id,food_item,quantity,price,amount):
        self.order_id=order_id
        self.food_item=food_item
        self.quantity=quantity
        self.price=price
        self.amount=amount

    def calculate_total_amount(self):
        self.amunt=self.quantity*self.price
        print(f"total amount :{self.amount}")
    def order_details(self):
        print(f"order details:\norder id:{self.order_id}\nfood item:{self.food_item}\nquantity:{self.quantity}\nprice:{self.price}")

# c1=restaurant(101,"spice garden","kochi")
# c1.restaurant_info()

o1=order(1,"biriyani",2,100,100)
o1.order_details()
o1.calculate_total_amount()
        
