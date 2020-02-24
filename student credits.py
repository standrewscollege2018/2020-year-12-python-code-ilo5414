#This program is for a student credit checklist

#student names list
students = [["Harry",2],  ["Tom", 4], ["Jamie", 6], ["Izzy",8],  ["Max",10],  ["Alexa",12],  ["Georgia",14]]

#Menu function, this creates a menu for the users where they have a choice between 5 different options
#the programme can do. the programme displays the options in a loop. The users are then asked to
#input a number that represents one of the options availible. The user input is then matched and
#connected to a function that takes the user to that option they selected. This is inside a try statement
#with if statements to see what option the user selected, an else statement at the end provides error catching. 
#the except statement catches any input that is not a number. 
def menu():
    while True:

        #displaying all the option availble for the user to select
        print("")
        print("Welcome to the student credit database")
        print("please select one of the following options")
        print("1. Show list of student and credits")
        print("2. Add new student")
        print("3. Delete student")
        print("4. Update details")
        print("5. Exit")

        #using a try and except statement to error catch unwanted inputs
        try:
            #reciveing users input
            option_select = int(input())

            #using if statments to connect the users option input to the option function
            if option_select == 1:
                show_list()

            elif option_select == 2:
                add_new()

            elif option_select == 3:
                delete_std()

            elif option_select == 4:
                update()

            elif option_select == 5:
                exit()
            #error catching for number inputs that are not one of the options
            else:
                print("Please enter a number between 1 and 5")

        #error catching for inputs that are not integers
        except:
            print("error, please enter an interger")


#displaying the list function
def show_list():
    for index in range(0, len(students)):
        print("{}. {} - Credits: {}".format(index+1, students[index][0], students[index][1]))

        

#adding new student function
def add_new():

    repetition = int(input("How many new students do you wish to add?:"))
    for i in range (0, repetition):
        student_name = input("Enter student's name")
        student_credits = int(input("Enter number of credits"))

        new_student = [student_name, student_credits]
        students.append(new_student)

        print(new_student, "Has been added")

    

#deleting student function
def delete_std():
    show_list()
    repetition = int(input("How many new students do you wish to delete?:"))
    for i in range (0, repetition):
        student_number = int(input("Please Enter the number of the student you wish to delete?:"))
        print(students[student_number-1],"is being deleted")
        del(students[student_number-1])

    


#updating student information function
def update():
    show_list()
    ask = True
    while ask == True:
        try:
            repetition = int(input("How many new students do you wish to update?:"))
            if repetition in range(1, len(students)):
                ask = False

            else:
                print("ERROR! Please enter a valid number")
                print("")

        except:
            print("ERROR! Please enter a valid integer")
            print("")



    for i in range (0, repetition):

        ask = True
        while ask == True:
            try:
                student_number = int(input("Please Enter the number of the student you wish to update?:"))
                if student_number in range(1, len(students)):
                    ask = False

                else:
                    print("ERROR! Please enter a valid number")
                    print("")

            except:
                print("ERROR! Please enter a valid integer")
                print("")

        
    ask = True
    while ask == True:
        try:
            print("")
            print("What would you like to update?")
            print("1. Students name")
            print("2. Students credits")
            print("3. Both")
            update_option = int(input())
            if update_option in range(1,4):
                ask = False

                #Update option one
                if update_option == 1:
                    new_name = input("Enter new name")
                    students[student_number-1][0] = new_name


                #Update option two   
                elif update_option == 2:
                    print("Please select one of the following options")
                    print("1. Change the whole total credits")
                    print("2. Add credits to total")
                    
                    credit_update = int(input())
                    #to CHANGE the total amount of credits
                    if credit_update == 1:
                        
                        ask = True
                        while ask == True:
                            try:
                                new_credits = int(input("Enter new number of credits"))
                                if new_credits in range(0,120):
                                    ask = False
                                    
                                    students[student_number-1][1] = new_credits

                                else:
                                    print("Please enter a vaild amount of credits")
                                    
                            except:
                                print("Please enter a valid integer")

                     #to ADD to the total amount of credits   
                    elif credit_update == 2:

                        ask = True
                        while ask == True:
                            try:
                                add_credits = int(input("Enter the number of credits you wish to add:"))
                                if add_credits in range(1,120):
                                    ask = False
                                    
                                    current_credits = students[student_number-1][1]
                                    new_total = current_credits + add_credits   
                                    students[student_number-1][1] = new_credits

                                else:
                                    print("Please enter a vaild amount of credits")
                                    
                            except:
                                print("Please enter a valid integer")

                                
                        add_credits = int(input("Enter the number of credits you wish to add:"))
                        current_credits = students[student_number-1][1]
                        new_total = current_credits + add_credits

                        students[student_number-1][1] = new_total

                    else:
                        print("Error!, please enter a valid number")


               #Update option three
                else:
                    new_name = input("Enter new name")
                    students[student_number-1][0] = new_name
                    
                   print("Please select one of the following options")
                    print("1. Change the whole total credits")
                    print("2. Add credits to total")
                    
                    credit_update = int(input())
                    #to CHANGE the total amount of credits OPTION 3
                    if credit_update == 1:
                        
                        ask = True
                        while ask == True:
                            try:
                                new_credits = int(input("Enter new number of credits"))
                                if new_credits in range(0,120):
                                    ask = False
                                    
                                    students[student_number-1][1] = new_credits

                                else:
                                    print("Please enter a vaild amount of credits")
                                    
                            except:
                                print("Please enter a valid integer")

                     #to ADD to the total amount of credits in (OPTION 3)
                    elif credit_update == 2:

                        ask = True
                        while ask == True:
                            try:
                                add_credits = int(input("Enter the number of credits you wish to add:"))
                                if add_credits in range(1,120):
                                    ask = False
                                    
                                    current_credits = students[student_number-1][1]
                                    new_total = current_credits + add_credits   
                                    students[student_number-1][1] = new_credits

                                else:
                                    print("Please enter a vaild amount of credits")
                                    
                            except:
                                print("Please enter a valid integer")

                                
                        add_credits = int(input("Enter the number of credits you wish to add:"))
                        current_credits = students[student_number-1][1]
                        new_total = current_credits + add_credits

                        students[student_number-1][1] = new_total

                    else:
                        print("Error!, please enter a valid number")
                        
                    

            else:
                print("Please enter a number between 1 and 3")
                print("")

        except:
            print("Please enter a valid integer")
            print("")
            

        
menu()
















        


        

