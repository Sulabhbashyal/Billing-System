
class ElectronicsShopBillCalculator:
    def __init__(self):
        self.products = {}
        self.total_bill = 0

    def add_product(self, product_name, price):
        self.products[product_name] = price

    def calculate_bill(self, purchased_items):
        self.total_bill = sum(self.products[item] for item in purchased_items)

    def display_bill(self):
        print('\n')
        print("**********************")
        print("   ECSC Group   ")
        print("**********************\n")
        print("Purchased Items:")
        for item, price in self.products.items():
            print(f"{item}: ₹{price:.2f}")
        print("\nTotal Bill: ₹{:.2f}".format(self.total_bill))
        print("\nThank you for shopping with us!")

    def display_available_products(self):
        print("Available Products:")
        for item, price in self.products.items():
            print(f"{item}: ₹{price:.2f}")

    def add_new_product(self, product_name, price):
        if product_name in self.products:
            print(f"{product_name} already exists in the product list.")
        else:
            self.add_product(product_name, price)
            print(f"{product_name} added successfully!")


shop = ElectronicsShopBillCalculator()

shop.add_product("Asus Laptop", 1_30_000)
shop.add_product("Dell Laptop", 80_000)
shop.add_product("Cannon Camera", 1_00_000)
shop.add_new_product("Poco Mobile", 20_000)

shop.display_available_products()

purchased_items = ["Asus Laptop", "Dell Laptop",
                   "Cannon Camera", "Poco Mobile"]

shop.calculate_bill(purchased_items)
shop.display_bill()
