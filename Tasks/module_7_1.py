

class Product():
    def __init__(self, _name, _weight, _category):
        self.name = _name
        self.weight = _weight
        self.category = _category
    
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop():
    __file_name = 'products.txt'

    def __init__(self) -> None:
        _file = open(self.__file_name, 'a')
        ##_res = _file.read()
        _file.close()
        
    def get_products(self):
        _file = open(self.__file_name, 'r')
        _res = _file.read()
        #print(_res, type(_res))
        _file.close()
        return _res
    
    def add(self, *products):
        _volume = self.get_products()

        for i in products:
            if i.name in _volume:
                print(f"{i.name} is in the shop")
            else:
                _volume += f"{i}\n"

        _file = open(self.__file_name, 'w')
        _file.write(_volume)
        _file.close()




if __name__ == '__main__':

    shop = Shop()

    p1 = Product('Potato', 50.0, 'Vagetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vagetables')

    print(p2)

    shop.add(p1, p2, p3)

    print(shop.get_products())

