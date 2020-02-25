#Book Store Program


book_list[[harry potter, j.k.rowling, 10], [the giver, lois lowry, 20], [gone, michael grant,30]]

#Main Menu Function
def menu()

    while True:
        #displaying the options for the program
        print("Main MENU")
        print("1. Find Book")
        print("2. Add Book")
        print("3.Edit Book")
        print("4. Delete Book)
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

            
