#This will be my class
class Product:
    def __init__(self, name, productID, rPrice, sPrice):
        self.__name = name
        self.__productID = productID
        self.__rPrice = rPrice
        self.__sPrice = sPrice

    def getName(self):
        return self.__name
    def getProductID(self):
        return self.__productID
    def getrPrice(self):
        return self.__rPrice
