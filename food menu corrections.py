import time


meal1 = "amphitheatre spaghetti"
meal2 = "beans cake"
meal3 = "beans"
meal4 = "dli special rice"
sup1 = "turkey"
sup2 = "chicken"
sup3 = "meat"
sup4 = "fish"
dup1 = "bread"
dup2 = "pap"
dup3 = "custard"
print('''        SLIMANY ADVANCED FOOD AI IS LOADING....................''')
time.sleep(3)
print('''                 WELCOME TO SLIMANY FOOD CAFETERIA........''')
print('''         AVAILABLE FOODS WILL BE DISPLAYED SHORTLY....''')
time.sleep(3)
print(
    f'WELCOME ONCE AGAIN TO SLIMANY CANTEEN \nWe have the following meals listed below:\n1. {meal1}\n2. {meal2}\n3. {meal3}\n4. {meal4}')

meal_choice = int(input("Choose a breakfast item: "))
if meal_choice == 1:
    Meal = meal1
    print(f'We have the following food supplements for preferred {Meal} \n 1. {sup1} \n 2. {sup2} \n 3. {sup3} \n 4. {sup4}')
    sup = int(input("Choose a type of sup: "))
    if sup == 1:
        sup = sup1
    elif sup == 2:
        sup = sup2
    elif sup == 3:
        sup = sup3
    elif sup == 4:
        sup = sup4
    print(f'You choose {Meal} and {sup}')
elif meal_choice == 4:
    Meal = meal4
    print(f'We have the following food supplements for preferred {Meal} \n 1. {sup1} \n 2. {sup2} \n 3. {sup3} \n 4. {sup4}')
    sup = int(input("Choose a type of sup: "))
    if sup == 1:
        sup = sup1
    elif sup == 2:
        sup = sup2
    elif sup == 3:
        sup = sup3
    elif sup == 4:
        sup = sup4
    print(f'You choose {Meal} and {sup}')
if meal_choice == 2:
    Meal = meal2
    print(f'We have the following food supplements for preferred {Meal} \n 1. {dup1} \n 2. {dup2} \n 3. {dup3}')
    dup = int(input("Choose a type of supplement: "))
    if dup == 1:
        dup = dup1
    elif dup == 2:
        dup = dup2
    elif dup == 3:
        dup = dup3
    print(f'You choose {dup} and {Meal}')
elif meal_choice == 3:
    Meal = meal3
    print(f'We have the following food supplements for preferred {Meal} \n 1. {dup1} \n 2. {dup2} \n 3. {dup3}')
    dup = int(input("Choose a type of supplement: "))
    if dup == 1:
        dup = dup1
    elif dup == 2:
        dup = dup2
    elif dup == 3:
        dup = dup3
    print(f'You choose {Meal} and {dup}')

time.sleep(3)
print("THANKS FOR DINING WITH US")