# casual breakfast menu

# the user can choose either of the 4 items


print("1. korede spag")
print("2. akara")
print("3. beans")
print("4. iya moria special")
# this allows the user to input a number between 1-4
MainChoice = int(input("Choose a breakfast item: "))
if (MainChoice == 2):
    Meal = "akara"
elif (MainChoice == 3):
    Meal = "beans"
if (MainChoice == 1):
    print("1. turkey")
    print("2. chicken")
    print("3. meat")
    print("4. fish")
    supplement = int(input("Choose a type of supplement: "))
    if (supplement == 1):
        print("You chose korede spag with turkey supplement.")
    elif (supplement == 2):
        print("You chose korede spag with chicken supplement.")
    elif (supplement == 3):
        print("You chose korede spag with meat supplement.")
    elif (supplement == 4):
        print("You chose korede spag with fish supplement.")
    else:
        print("We have korede spag, but not that kind of supplement.")

elif (MainChoice == 2) or (MainChoice == 3):
    print("1. bread")
    print("2. pap")
    print("3. Custard")
    Topping = int(input("Choose a supplement: "))
    if (Topping == 1):
        print("You chose " + Meal + " with bread.")
    elif (Topping == 2):
        print("You chose " + Meal + " with pap.")
    elif (Topping == 3):
        print("You chose " + Meal + " with custard .")
    else:
        print("We have " + Meal + ", but not that supplement. ")

elif (MainChoice == 4):
    print("You chose iya moria special.")
else:
    print("We don't serve that breakfast item!")