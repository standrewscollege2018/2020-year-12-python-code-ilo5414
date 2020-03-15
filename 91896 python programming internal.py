""" 91896 Level 2 acheviement standard 2.7"""
""" Basic local resturant software """
""" Enable resturant to veiw a summary and total cost of an order """

entree = [["Dumplings",  8], ["Wontons", 8], ["Spring Rolls", 8], ["Prawns", 8]]
main = [["Bao Buns", 20], ["Chicken Stirfry", 20], ["Ramen Bowl", 20], ["Sushi" ,20]]
dessert = [["Ice cream sundae", 10], ["Crepes", 10], ["Waffles", 10], ["Sorbet", 10]]
specials = [["prawn crackers",  6]]
order = []
PASSWORD = "password123"
MENU_OPTION_MAX = 8

#menu
print("----MENU----")
print("(1). Entree")
print("(2). Main")
print("(3). Dessert")
print("(4). Specials")
print("(5). Edit Menu")
print("(6). Edit Order")
print("(7). Clear Order")
print("(8). Exit")

#error catching for option input
ask = True
while ask == True:
    try:
        #option input
        option_selection = int(input("type here"))
        #boundry for option input
        if option_selection in range(1, MENU_OPTION_MAX+1):
            #if input is valid, loop is set to false
            ask = False
        #catching incorrect integer errors
        else:
            print("ERROR! please enter a valid option")
    #catching errors that are not integer e.g. symbols, text ect
    except:
        print("ERROR! please enter a valid integer")

print(option_selection)




