#Book Store Program


book_list = [["harry potter", "j.k.rowling", 10], ["the giver", "lois lowry" ,20], ["gone", "michael grant",30]]

#Main Menu Function
def menu():

    while True:
        #displaying the options for the program
        print("Main MENU")
        print("1. Find Book")
        print("2. Add Book")
        print("3.Edit Book")
        print("4. Delete Book")
        print("5. Exit")

        try:
            #user input allowing them to select an option
            option_select = int(input())

            #using if statments to connect the users option input to the option function
            if option_select == 1:
                find_book()

            elif option_select == 2:
                add_book()

            elif option_select == 3:
                edit_book()

            elif option_select == 4:
                delete_book()

            elif option_select == 5:
                exit()
            #error catching for number inputs that are not one of the options
            else:
                print("Please enter a number between 1 and 5")
        #error catching for inputs that are not integers
        except:
            print("error, please enter an interger")



#def find_book():

####################################################################
#add book funtion
def add_book():
    #asking the users how many books they wish to add
    print("How many books would you like to add?")

    #boolean while loop to help with error catching
    ask = True
    while ask == True:
        try:
            #user input for how many books they wish to add
            repetition = int(input("type here"))
            #limit to 100 books that can be added at one time
            if repetition in range(0,101):
                #if the user enters an input within thhe min and max of the limit
                #the while loop is set to false and the next part of the function is open
                ask = False

            #catching inputs that is not within the limit
            else:
                print("Error 1")

        #catching inputs that not integers
        except:
            print("Error 2")

    #user input for the name of the new book being added
    print("please enter the name of the book")
    name = input("type here")

    #user input for the name of the author of the new book being added
    print("please enter the name of the author")
    author = input("type here")

    #user input for the price of the new book being added
    print("please enter the price of the book")
    #boolean while loop around the input to make sure that the right number is inputted
    ask = True
    while ask == True:
        try:
            #input for the price
            price = int(input("type here"))
            #price inputted can't be over 200
            if price in range(1,201):
                #if input is correct, loop is set to false and function carries on
                ask = False
            #catching inputs that is not within the limit
            else:
                print("Error 1")
        #catching inputs that not integers
        except:
            print("Error 2")
    #creating a new sub list to append/ add to the original list
    new_book = [name, author, price]
    book_list.append(new_book)

    #displaying the new book being added
    print(new_book, "has been added")
            


#def edit_book():


#def delete_book():



menu()

            
