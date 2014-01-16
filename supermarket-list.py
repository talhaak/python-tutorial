# Aim is the learning lists and dictionaries with using for loop.
# İnitializing dictionaries and lists.
prices = { 'banana' : 4 , 'apple' : 2 , 'orange' : 1.5 , 'pear' : 3 }
stock = { 'banana' : 6 , 'apple' : 0 , 'orange' : 32 , 'pear' : 15 }
shopping_list = ["banana", "orange", "apple"]

# Printing the price and stock condition of each products.
for key in (prices and stock) :
    print(key)
    print('price: ' + str(prices[key]))
    print('stock: ' + str(stock[key]))
    print()

#Finding total value of products in stocks.
money = 0
for key in (prices and stock) :
    
    money += prices[key] * stock[key]
print('Total value of products in stock: ' + str(money))   

# Computing total cost of shopping list.
def compute_bill (shopping_list) :
    total = 0
    for food in shopping_list  :
        if stock[food] == 0 :
            total = total 
        else : 
            total = total + prices[food]
            stock[food] = stock[food] - 1
    
    return total    

  