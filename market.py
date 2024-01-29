#This will be my class
class Product:
    def __init__(self, name, productID, rPrice, sPrice):
        self.__name = name
        self.__productID = productID
        self.__rPrice = rPrice
        self.__sPrice = sPrice
#Below are accessor methods (get methods)
    def getName(self):
        return self.__name
    def getProductID(self):
        return self.__productID
    def getrPrice(self):
        return self.__rPrice
    def getsPrice(self):
        return self.__sPrice
    def getPercent(self):
        return ((self.__rPrice - self.__sPrice) / self.__rPrice)
    
#Below are mutator methods
    def setName(self, name):
        self.__name = name
    
    def setProductID(self, productID):
        self.__productID = productID

    def setrPrice(self, rPrice):
        self.__rPrice = rPrice

    def setsPrice(self, sPrice):
        self.__sPrice = sPrice
    
#Method to show the state of the class
    def __str__(self):
        return ("{0:14s}{1:^9s}${2:<9,.2f}${3:<10,.2f}{4:<8,.2%}".format(self.__name,self.__productID, self.__rPrice, self.__sPrice, (self.__rPrice - self.__sPrice) / self.__rPrice))
    
