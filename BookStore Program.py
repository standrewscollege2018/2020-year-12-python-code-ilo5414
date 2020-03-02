#Book Store Program


book_list = [["harry potter", "j.k.rowling", 10], ["the giver", "lois lowry" ,20], ["gone", "michael grant",30]]
counter = 0 
#Main Menu Function
def menu():

    while True:
        #displaying the options for the program
        print("Main MENU")
        print("1. Find Book")
        print("2. Add Book")
        print("3. Edit Book")
        print("4. Delete Book")
        print("5. Display books")
        print("6. Exit")

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
                display()

            elif option_select == 6:
                exit()
                
            #error catching for number inputs that are not one of the options
            else:
                print("Please enter a number between 1 and 5")
        #error catching for inputs that are not integers
        except:
            print("error, please enter an interger")


####################################################################
#displaying the books in the system
def display():
    #creating a loop that goes through and displays each book from in postion of 0 to the end of the list
    for index in range(0,len(book_list)):
    
        #printing and formating the names and parts of the books being displayed
        print("{}. {} By:  {}, Price: ${}".format(index+1, book_list[index][0], book_list[index][1], book_list[index][2]))

    print("")
    
   
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
                #if the user enters an input within the min and max of the limit
                #the while loop is set to false and the next part of the function is open
                ask = False

            #catching inputs that is not within the limit
            else:
                print("Error 1")

        #catching inputs that not integers
        except:
            print("Error 2")

    for i in range(0, repetition):
    
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



def delete_book():
    #displaying the books in the system
    display()

    #using a loop to error catch unwanted inputs
    print("How many books do you wish to delete")
    #calling the rep function and bringing out the repetition value 
    repetition = rep()
    
    #fixed loop to repeat the delete book component as many times as the user inputted in previous input
    for i in range(0, repetition):
    
        print("please enter the book reference of the book you wish to delete")
        #calling the book reference function
        book_ref = book_refer()
       
        


        #displaying the book being deleted
        print(book_list[book_ref-1],"is being deleted")
        #deleting the book
        del(book_list[book_ref-1])
        
        
def book_refer():
    ask = True
    while ask == True:
        try:
            #user input for the book they wish to adapt
            book_ref = int(input("type here"))
            #setting a boundry to users can only enter a number that represents a book
            if book_ref in range(1, len(book_list)+1):
                #if input is valid the loop is set to false and the function carries on.
                ask = False
                #returning the book reference
                return book_ref

            #catching errors that are integer
            else:
                print("Error 1")
        #catching errors that are not integer
        except:
                print("Error 2")
         

#function to control how many times a functions repeats 
def rep():
    ask = True
    while ask == True:
        try:
            #getting the users input for how many books they want to alter
            repetition = int(input("type here?"))

            #creating an input boundry so that no more than the amount of books there are can be changed
            if repetition in range(1, len(book_list)+1):
                #if the input is valid then the loop is set too false and the function carries on
                ask = False
                #returning the repetition input
                return repetition

            #catching incorrect integer input
            else:
                print("Error 1")
                print("")
                
        #catching incorrect inputs thats not string
        except:
            print("Error 2")
            print("")

    


menu()

            
