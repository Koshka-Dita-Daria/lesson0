class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                products = file.read()
            return products
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products()
        existing_names = set()
        
        for line in existing_products.splitlines():
            if line:
                product_name = line.split(',')[0].strip()
                existing_names.add(product_name)

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in existing_names:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{str(product)}\n')
                    existing_names.add(product.name)

sl = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

sl.add(p1, p2, p3)
print(sl.get_products())
