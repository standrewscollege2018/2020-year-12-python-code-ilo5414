#This program is for a student credit checklist

#student names list
students = [["Harry",2],  ["Tom", 4], ["Jamie", 6], ["Izzy",8],  ["Max",10],  ["Alexa",12],  ["Georgia",14]]

#Menu function, this creates a menu for the users where they have a choice between 5 different options
#the programme can do. the programme displays the options in a loop. The users are then asked to
#input a number that represents one of the options availible. The user input is then matched to and
#connected a function that takes the user to that option they selected. This is inside a try statement
#with if statements to see what option the user selected, an else statement at the end provides error catching. 
#the except statement catches any input that is not a number. 
def menu():
    while True:
        print("Welcome to the student credit database")
        print("please select one of the following options")
        print("1. Show list of student and credits")
        print("2. Add new student")
        print("3. Delete student")
        print("4. Update details")
        print("5. Exit")

        try:
            option_select = int(input())
            if option_select == 1:
                show_list()

            elif option_select == 2:
                add_new()

            elif option_select == 3:
                delete_std()

            elif option_select == 4:
                update()

            else:
                print("Please enter a number between 1 and 4")

        except:
            print("error, please enter an interger")



def show_list():
    for index in range(0, len(students)):
        print("{}. {} - Credits: {}".format(index+1, students[index][0], students[index][1]))


def add_new():
    student_name = input("Enter student's name")
    student_credits = int(input("Enter number of credits"))

    new_student = [student_name, student_credits]
    students.append(new_student)


def delete_std():
    show_list()
    std_number = int(input("Enter student number you wish to delete:"))
    del(students[std_num-1])


menu()

















        


        

