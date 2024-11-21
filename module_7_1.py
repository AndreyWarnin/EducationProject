class Product:
    name = None
    weight = 0.0
    category = None

    def __init__(self, new_name, new_weight, new_category):
        self.name = new_name
        self.weight = new_weight
        self.category = new_category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        shop_products = self.get_products()
        for product in products:
            if shop_products.__contains__(product.__str__()):
                print(f'{product} уже есть в магазине')
            else:
                new_product = product.__str__() + '\n'
                shop_products += new_product
        file = open(self.__file_name, 'w')
        file.write(shop_products)
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())