# assign4.py

# Product Class
class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    def __eq__(self, other): 
         if isinstance(other, Product):
             if ((self._name == other._name and self._price == other._price) and (self._category==other._category)):
                return True
             else:
                return False
         else:
            return False

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep

# Inventory Class

class Inventory:
    def __init__(self):
        self.inventory_dict = {}

    def add_to_productInventory(self, productName, productPrice, productQuantity):
        self.inventory_dict[productName] = {'price': productPrice, 'quantity': productQuantity}

    def add_productQuantity(self, nameProduct, addQuantity):
        self.inventory_dict[nameProduct]['quantity'] += addQuantity

    def remove_productQuantity(self, nameProduct, removeQuantity):
        if self.inventory_dict[nameProduct]['quantity'] >= removeQuantity:
            self.inventory_dict[nameProduct]['quantity'] -= removeQuantity
            return "Successful"
        else:
            return "The requested quantity to be removed from cart exceeds what is in the cart"

    def get_productPrice(self, nameProduct):
        return self.inventory_dict[nameProduct]['price']

    def get_productQuantity(self, nameProduct):
        return self.inventory_dict[nameProduct]['quantity']

    def display_Inventory(self):
        for product, info in self.inventory_dict.items():
            print(f"{product}, {info['price']}, {info['quantity']}")

# Shopping Cart Class

class ShoppingCart:
    def __init__(self, buyerName, inventory):
        self.buyerName = buyerName
        self.inventory = inventory
        self.cart = {}

    def add_to_cart(self, nameProduct, requestedQuantity):
        if self.inventory.get_productQuantity(nameProduct) >= requestedQuantity:
            if nameProduct in self.cart:
                self.cart[nameProduct] += requestedQuantity
            else:
                self.cart[nameProduct] = requestedQuantity
            self.inventory.remove_productQuantity(nameProduct, requestedQuantity)
            return "Filled the order"
        else:
            return "Can not fill the order"

    def remove_from_cart(self, nameProduct, requestedQuantity):
        if nameProduct not in self.cart:
            return "Product not in the cart"
        elif requestedQuantity > self.cart[nameProduct]:
            return "The requested quantity to be removed from cart exceeds what is in the cart"
        else:
            self.cart[nameProduct] -= requestedQuantity
            self.inventory.add_productQuantity(nameProduct, requestedQuantity)
            return "Successful"

    def view_cart(self):
        total_price = 0
        
        for product, quantity in self.cart.items():
            price = self.inventory.get_productPrice(product)
            total_price += price * quantity
            print(f"{product} {quantity}")
        print(f"Total: {total_price}")
        print(f"Buyer Name: {self.buyerName}")

# Product Catalog Class

class ProductCatalog:
    def __init__(self):
        self.catalog = []

    def addProduct(self, product):
        self.catalog.append(product)

    def price_category(self):
        low_prices = medium_prices = high_prices = 0
        for product in self.catalog:
            price = product.get_price()
            if price <= 99:
                low_prices += 1
            elif 100 <= price <= 499:
                medium_prices += 1
            else:
                high_prices += 1
        print(f"Number of low price items: {low_prices}")
        print(f"Number of medium price items: {medium_prices}")
        print(f"Number of high price items: {high_prices}")

    def display_catalog(self):
        for product in self.catalog:
            print(f"Product: {product.get_name()} Price: {product.get_price()} Category: {product.get_category()}")

# NON-CLASS FUNCTION
def populate_inventory(filename):
    inventory = Inventory()
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, price, quantity, _ = line.strip().split(',')
                inventory.add_to_productInventory(name, int(price), int(quantity))
    except FileNotFoundError:
        print(f"Could not read file: {filename}")
    return inventory

# NON-CLASS FUNCTION
def populate_catalog(fileName):
    catalog = ProductCatalog()
    try:
        with open(fileName, 'r') as file:
            for line in file:
                name, price, _, category = line.strip().split(',')
                product = Product(name, int(price), category)
                catalog.addProduct(product)
    except FileNotFoundError:
        print(f"Could not read file: {fileName}")
    return catalog