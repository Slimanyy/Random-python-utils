import time
from food_utils import Menu

item1 = Menu("Korede spaghetti", 1500)
item2 = Menu("Iya moria rice", 600)
item3 = Menu("TY spaghetti", 1000)
item4 = Menu("Biobaku spaghetti", 1050)

food_list = [item1, item2, item3, item4]
num = 0
print('''        SLIMANY ADVANCED FOOD AI IS LOADING....................
                    WELCOME TO SLIMANY FOOD CAFETERIA........
                        THANKS FOR DINING WITH US 
                    AVAILABLE FOODS WILL BE DISPLAYED SHORTLY....''')
time.sleep(4)
print("We have the following items :")

for food in food_list:
    print('Input ' + str(num) + '. for ' + food.info())
    time.sleep(2)
    num += 1
print("ALL AVAILABLE ITEMS ARE SHOWN ABOVE")
order = int(input("Select preferred food choice: "))
order_selected = food_list[order]
print('You choose:  ' + order_selected.name)

order_count = int(input('How many packs of ' + order_selected.name + ' would you like to order ? : '))

if order_count <= 1:
    print("You ordered  a pack of " + order_selected.name)  # + str(order_count)
else:
    print("You ordered " + str(order_count) + ' packs of ' + order_selected.name)

order_price = order_selected.total_price(order_count)
print('Your bill is #' + str(order_price))
