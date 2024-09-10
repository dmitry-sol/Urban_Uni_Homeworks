# module_7_1
# "Режимы открытия файлов"

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
        file = open(self.__file_name, 'r')
        file_read = file.read()
        file.close()
        return file_read

    def add(self, *products):
        len_ = len(products)

        file = open(self.__file_name, 'r')
        products_ = file.read()
        file.close()

        file = open(self.__file_name, 'a')

        i = 0
        while i < len_:
            if products[i].name not in products_:
                file.write(str(products[i]) + '\n')
                i += 1
            else:
                print(f'Продукт {products[i]} уже есть в магазине')
                i += 1
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
