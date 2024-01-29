#This program will 
import market #This is my class, it is getting imported
import pickle#Imports pickle
def main():#Declares main function
        
    GetProductData()#Void method call for the GetProductData
    ShowDiscount()

def GetProductData():#This is a method/function header
    #Initializes local vars
    key = "Y"
    name = ""
    productID = ""
    rPrice = 0.00
    sPrice = 0.00
    outFile = ""
    entryList = []#Initializes list
    
    outFile = open("marketinfo.dat", "wb")#creates and opens a file marketinfo.dat in write binary mode
    while(key.upper() == "Y"):#While the key variable equals y, the loop continues, when the user changes it, it breaks out of the loop
        name = str(input("Enter a product name: "))
        while True: #Input validation loop
            productID = str(input("Enter the product ID number: "))
            if len(productID) != 5:#if the length of product is not equal 5 it will print the statement below and loop back for another try at input
                print("The product number MUST be 5 characters in length \nPlease enter again")
            else:
                break#Breaks out of loop
        rPrice = float(input("Enter the retail price of the product $"))
        sPrice = float(input("Enter the sale price of the product $"))
        
        entry = market.Product(name, productID, rPrice, sPrice)
        entryList.append(entry)
    
        key = input("Do you want to enter another product? If so, enter y/Y: ")#check to see if the user wants to enter more products
    pickle.dump(entryList, outFile) #dumps the list to the outFile
    outFile.close()#closes outfile
        
def ShowDiscount():#This is a method/function header
    outFile = open("marketinfo.dat", "rb")#Opens marketinfo.dat in read binary 
    #Initializes local vars below
    name = ""
    productID = ""
    rPrice = 0.00
    sPrice = 0.00
    
    outputList = []#Initializes a list
    outputList = pickle.load(outFile)#loads the outfile
    outFile.close()#Closes file
    #print("{0:16s} {1:1s} {2:^9s} {3:1s} {4:9s} {5:1s} {6:5s} {7:1s} {8:8s}".format
          #("Product", "", "Product", "", "Retail", "", "Sale", "", "Percent"))#Headers
    #print("{0:16s} {1:1s} {2:^9s} {3:1s} {4:9s} {5:1s} {6:5s} {7:1s} {8:8s}".format
          #(" Name", "", "ID", "", "Price", "", "Price", "", "Discount"))#Headers
    #print("{0:16s} {1:1s} {2:^9s} {3:1s} {4:9s} {5:1s} {6:5s} {7:1s} {8:8s}".format
          #("----------", "", "-------", "", "------", "", "-----", "", "--------"))#Headers

    print("{0:14s}{1:^9s}{2:10s}{3:10s}{4:10s}".format
          ("Product","Product","Retail","Sale","Percent"))#Headers
    print("{0:14s}{1:^9s}{2:10s}{3:10s}{4:10s}".format
          (" Name","ID","Price","Price","Discount"))#Headers
    print("{0:14s}{1:^9s}{2:10s}{3:10s}{4:10s}".format
          ("----------","-------","------","-----","--------"))#Headers

    
    for entry in outputList:#EOF loop
        print(entry)#Prints 



main()#Calls main function
