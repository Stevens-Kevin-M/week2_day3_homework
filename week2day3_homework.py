# Shopping Cart (Exercise 1)
​
def shoppingCart():
    emptydictionary = {}
    while True:
        addOrRemoveItem = input("Would you like to add or remove an item to/from your cart? ")
        if addOrRemoveItem.lower()== 'quit':
            break
        if addOrRemoveItem.lower()== 'add':
                whatItemAdd = input("What item would you like to add? ")
                emptydictionary[whatItemAdd] = 1
        if addOrRemoveItem.lower() == 'remove':
                whatItemRem = input("What item would you like to remove? ")
                if emptydictionary[whatItemRem]:
                    del emptydictionary[whatItemRem]
        else:
            askAboutCart = input("Would you like to view your cart? ")
        if askAboutCart.lower()== 'yes':
            print(sorted(emptydictionary.keys()))
        else:
            continue
    
    print(emptydictionary)
            
shoppingCart()
​
​
​
# Modules - Exercise 2
​
import math
​
def squared(l,w):
    area = l*w
    return area
​
def circleCirc(radius):
    circumference = 2*math.pi*radius
    return circumference
​
# Module pull below
​
%run my_module.py
​
import my_module
​
squared(20,5)
​
circleCirc(1)