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

################################################################################
#displaying the list function
def show_list():
    #creating a conditional loop to print out each student in the list
    #between the index of 0 and the total length of the list
    for index in range(0, len(students)):
        
        #printing and formatting the output (the names and credits of the students
        #curly brackets representing the information in the format bracket.
        print("{}. {} - Credits: {}".format(index+1, students[index][0], students[index][1]))

        
################################################################################
#adding new student function
#this function allows new students and their credits to be added to the list.
#multiple students can also be added at the same time.
def add_new():
    #using a while loop with boolean values to error catch unwanted/incorrect inputs
    ask = True
    while ask == True:
        try:
            #user input for how many new students the user wants to add
            #the input to be the amount of times this function repeats its self.
            repetition = int(input("How many new students do you wish to Add?:"))

            #creating a boundry for what inputs are excepted, no less than one
            #and no more than 231 (the rough size of a year group)
            if repetition in range(1, 231):
                
                #If the user enters a correct input between 1 and 231
                #the while loop is set to false and takes the input to the next part of the function
                ask = False

            #errors such as inputs that are not between 1 and 231 and caught here
            else:
                print("ERROR! Please enter a valid number")
                print("")
                
        #other unexpected errors such as string or symbols are caught here
        except:
            print("ERROR! Please enter a valid integer")
            print("")

    #loop repeated for as many times as the user inputed in the repetition input previously
    for i in range (0, repetition):
        #user inputting new students name
        student_name = input("Enter student's name")

        #using a while loop with boolean values to error catch unwanted/incorrect inputs
        ask = True
        while ask == True:
            try:
                #user input for the number of credits they wish to input for the new student
                student_credits = int(input("Enter number of credits"))

                #limit/boundry for how many credits can be added
                if student_credits in range(1,121):
                    #if input is within the limit loop is set to false and input is taken to the next part of the function
                    ask = False

                #errors such as inputs that are not between 1 and 121 are caught here
                else:
                    print("ERROR! Please enter a valid number")
                    print("")
                    
            #other unexpected errors such as string or symbols are caught here
            except:
                print("ERROR! Please enter a valid integer")
                print("")

        #new list made to append/add onto the original list
        new_student = [student_name, student_credits]
        students.append(new_student)

        #displaying the new student added
        print(new_student, "Has been added")

    
##############################################################################
#deleting student function
        #this function allows users to delete as many students between 1 and the length of the list
def delete_std():
    #displaying the list
    show_list()

    #using a while loop with boolean values to error catch unwanted/incorrect inputs
    ask = True
    while ask == True:
        try:
            #user input for how manystudents the user wants to delete
            #the input to be the amount of times this function repeats its self.
            repetition = int(input("How many new students do you wish to delete?:"))

            #creating a boundry for what inputs are excepted, no less than one
            #and no more than the length of the list
            if repetition in range(1, len(students)):
                #if input is within the limit/boundry, loop is set to false and input is taken to the next part of the function
                ask = False

             #errors such as inputs that are not between 1 and the length of the list are caught here
            else:
                print("ERROR! Please enter a valid number")
                print("")
        #other unexpected errors such as string or symbols are caught here
        except:
            print("ERROR! Please enter a valid integer")
            print("")

     #loop repeated for as many times as the user inputed in the repetition input previously
    for i in range (0, repetition):

        #using a while loop with boolean values to error catch unwanted/incorrect inputs
        ask = True
        while ask == True:
            try:
                #user input for how many students the user wants to delete 
                student_number = int(input("Please Enter the number of the student you wish to delete"))
                #setting a boundry for a maximum and minimum amount of students they can delete
                # 1 being the minimum and the length of the list being the maximum
                if student_number in range(1, len(students)):
                    #if input is within the boundry the while loop is set to false and the
                    #input is taken to the next part of the function
                    ask = False

                    #this prints the name and number of credits of the student being deleted
                    print(students[student_number-1],"is being deleted")
                    #this is deleteing the student selected
                    del(students[student_number-1])

                #errors such as inputs that are not between 1 and the length of the list are caught here
                else:
                    print("ERROR! Please enter a valid number")
                    print("")
                    
            #other unexpected errors such as string or symbols are caught here
            except:
                print("ERROR! Please enter a valid integer")
                print("")


        
    

    

###############################################################################
#updating student information function
    #this function allows users to update/change student names and credits that already preexsits in the list
    #they can update as many students between 1 and the total amount of students
    #they can update both the name and credits or each individually
    #and they can either change the total amount of credits or add to the number already there
def update():
    #displaying the list of students
    show_list()

    #using a while loop with boolean values to error catch unwanted/incorrect inputs
    ask = True
    while ask == True:
        try:
            #user input for how many times they want to update students
            repetition = int(input("How many new students do you wish to update?:"))

            #creating a limited between 1 and the length of the list
            if repetition in range(1, len(students)):
                #if input is within the min and max of the limit, the loop is set to false
                #and the input is taken to the next part of the function
                ask = False

            #errors such as inputs that are not between 1 and the length of the list are caught here
            else:
                print("ERROR! Please enter a valid number")
                print("")
                
         #other unexpected errors such as string or symbols are caught here
        except:
            print("ERROR! Please enter a valid integer")
            print("")


    #loop repeated for as many times as the user inputed in the repetition input previously
    for i in range (0, repetition):

        #using a while loop with boolean values to error catch unwanted/incorrect inputs
        ask = True
        while ask == True:
            try:
                #user input for what students they wish to update
                student_number = int(input("Please Enter the number OF the student you wish to update?:"))

                #limited on what students the user can update between 1 and the length of the list
                if student_number in range(1, len(students)):
                    #if input is within the min and max of the limit than the input is free to move onto the next part in th function
                    ask = False

                #errors such as inputs that are not between 1 and the length of the list are caught here
                else:
                    print("ERROR! Please enter a valid number")
                    print("")
                    
            #other unexpected errors such as string or symbols are caught here
            except:
                print("ERROR! Please enter a valid integer")
                print("")

    #using a while loop with boolean values to error catch unwanted/incorrect inputs     
    ask = True
    while ask == True:
        try:
            #displaying the update options
            print("")
            print("What would you like to update?")
            print("1. Students name")
            print("2. Students credits")
            print("3. Both")

            #update option input
            update_option = int(input())
            #creating a boundry to make sure users enter a number representing one of the options displayed above
            if update_option in range(1,4):
                #if user input is within the range, loop is changed to false and the input takes the user to the option they selected
                ask = False

                #Update option one
                #just allows the user to update the name of the student
                #if the user inputted 1, they are taken here
                if update_option == 1:
                    #user inputs the new name here
                    new_name = input("Enter new name")
                    #the number the user selected to change is pulled out here and made equal to the new name inputted
                    #noticing that the student_number has a -1 next to it becuase the list starts at zero but is displayed starting at 1
                    #the [0] is also needed to pull out the name portion in the list
                    students[student_number-1][0] = new_name


                #Update option two
                #just allows the user to update the whole amount of student credits or add credits
                #if the user inputted 2, they are taken here
                elif update_option == 2:
                    #displaying the option 
                    print("Please select one of the following options")
                    print("1. Change the whole total credits")
                    print("2. Add credits to total")




                    ask = True
                    while ask == True:
                        try:
                            #selection input for either changing the whole total credits or just adding credits
                            credit_update = int(input())
                            
                            #to CHANGE the total amount of credits
                            #if users inputed 1 they are taken here
                            if credit_update == 1:

                                #using a while loop with boolean values to error catch unwanted/incorrect inputs
                                ask = True
                                while ask == True:
                                    try:
                                        #input for the new amount of credits they want to replace the previous amount with
                                        new_credits = int(input("Enter new number of credits"))
                                        #setting a boundry so that the credits can't be changed to over 120 
                                        if new_credits in range(0,121):
                                            #if input is within the boundry then the loop is set to false and the function carries on 
                                            ask = False

                                            #the student selected by the user is pulled out and made equal to the new credits
                                            #noticing that the student_number is -1 because the displayed list starts from 1
                                            #where as the actual list starts from 0
                                            students[student_number-1][1] = new_credits

                                        #errors such as values inputted that are less or more than the limit are caught here
                                        else:
                                            print("Please enter a vaild amount of credits")
                                            
                                    #other errors such as string and symbols are caught here       
                                    except:
                                        print("Please enter a valid integer")

                             #to ADD to the total amount of credits
                            #if the user inputted 2 then they are taken here
                            elif credit_update == 2:
                                
                                #using a while loop with boolean values to error catch unwanted/incorrect inputs
                                ask = True
                                while ask == True:
                                    try:
                                        #user input for the amount of credits they wish to add to the credits already in the list
                                        add_credits = int(input("Enter the number of credits you wish to add:"))
                                        #creating a limit so no more than 119 credits can be added
                                        if add_credits in range(1,120):
                                            #if input is within the limit the loop is set to false and the function carries on
                                            ask = False

                                            #pulling out the the current credits the student has
                                            current_credits = students[student_number-1][1]
                                            #adding the new credits to the original credits 
                                            new_total = current_credits + add_credits
                                            #changing the original credits to the new total 
                                            students[student_number-1][1] = new_total

                                        #errors such as values inputted that are less or more than the limit are caught here
                                        else:
                                            print("Please enter a vaild amount of credits")
                                            
                                    #other errors such as string and symbols are caught here           
                                    except:
                                        print("Please enter a valid integer")
                                        
                            #if a number other than 1 or 2 is entered for the update option
                            else:
                                print("Error!, please enter a valid number")
                                
                        #Error handleing if string or symbols are inputted in the update option
                        except:
                            print("Error!, please enter a valid integer")


               #Update OPTION 3 (BOTH)
                else:
                    #letting the user input the new name
                    new_name = input("Enter new name")
                    #making the new name = the old one to change it
                    students[student_number-1][0] = new_name

                    #displaying the options for changing the credits
                    #all coding is the same as option 2 
                    print("Please select one of the following options")
                    print("1. Change the whole total credits")
                    print("2. Add credits to total")

                    ask = True
                    while ask == True:
                        try:
                            credit_update = int(input())
                            if credit_update in range(1,3):
                                ask = False

                            else:
                                print("Error!, please enter a valid number")

                        except:
                            print("Error!, please enter a valid integer")
                            
                    #to CHANGE the total amount of credits OPTION 3
                    if credit_update == 1:
                        
                        ask = True
                        while ask == True:
                            try:
                                new_credits = int(input("Enter new number of credits"))
                                if new_credits in range(0,121):
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
                                if add_credits in range(1,121):
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
            

#starting the menu code   
menu()
















        


        

