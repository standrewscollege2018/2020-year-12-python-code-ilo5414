#travel company program
#this program will calculate the total cost of a customers holiday from flights to accomodation costs

departure = [["Auckland", 0], ["Wellington", 50], ["Christchurch", 75]]
destination = [["Sydney", 326, 120], ["Tonga", 378, 40], ["Shanghai", 1436, 60], ["London", 2376, 80]]
trip = []
total_cost = 0

print("Welcome to Logie's Legendary travel service!")
print("We are so happy we can help you today")
print("")

print("Lets get your flights sorted!")
print("Where will you be departing New Zealand from?")
print("")

#displaying the departure options and the connecting flight costs
for index in range(0, len(departure)):
    print("{}. {} - connecting flight cost: ${}" .format(index+1, departure[index][0], departure[index][1]))

#getting users selection input
# in a conditional loop to catch errors both integer and other
# adding any connecting flight costs to total cost
ask = True
while ask == True:
    try:
        depart_option = int(input("type here"))
        #making sure users can only enter a number that represents one of the departure options
        if depart_option in range(1,4):
            #if input is valid the loop is set to false and the program carries on. 
            ask = False
            
        #catching inputs that are not 1 2 or 3 
        else:
            print("Please enter a valid option")
            
    #catching inputs that are not integer
    except:
        print("Please enter a number")

#appending the departure the user chose to the trip list
trip.append(departure[depart_option-1])
#adding connecting flight costs to the total cost
total_cost = trip[0][1]
#displaying the total cost
print("Total cost of your trip so far..$",total_cost)
#displaying where they are departing from
print("Looks like you are departing from..")
print(trip[0][0])
print("")


##########################################################################
#destination section
print("Time to select your destination!")
print("please select one of the following destinations")
print("")
#displaying the destination options and flight costs 
for index in range(0, len(destination)):
    print("{}. {} - connecting flight cost: ${}" .format(index+1, destination[index][0], destination[index][1]))


ask = True
while ask == True:
    try:
        destination_option = int(input("type here"))
        #making sure users can only enter a number that represents one of the destination options
        if destination_option in range(1,4):
            #if input is valid the loop is set to false and the program carries on. 
            ask = False
            
        #catching inputs that are not 1 2 or 3 
        else:
            print("Please enter a valid option")
            
    #catching inputs that are not integer
    except:
        print("Please enter a number")

#appending the destination to the trip list   
trip.append(destination[destination_option-1])
#calculating the new total cost
total_cost = total_cost + destination[destination_option-1][1]

#displaying the total cost
print("Total cost of your trip so far..$",total_cost)

#displaying the destination the user has chosen
print("Looks like you are heading to...")
print(trip[1][0])
print("")


###################################################################
#accomodation section
#displaying the trip details so far
print("Your exciting holiday from", trip[0][0], "to", trip[1][0],"is almost complete")
print("You now just need to select your accomodation!")
print("")

#displaying the per night price for the specific destination selected
print("Your accomodation per night in",  trip[1][0], "is", "${}".format(trip[1][2]))
print("However if you book 3 or more nights you get 20% off!!")

#getting user input for how many nights they would like to stay in a conditional to catch errors
print("How many nights would you like to stay in", trip[1][0])
ask = True
while ask == True:
    try:
        #user input for home many nights they wish to stay in their location
        nights = int(input("type here"))
        #setting a boundry so users can book a minimum of 1 night to a maximum of 10
        if nights in range(1,11):
            #if input is valid, the loop is set to false and program carries on
            ask = False
            
        #catching integer input errors, e.g. if the input is greater or less than the range
        else:
            print("please enter a valid number")

    #catching errors that are not integer.
    except:
        print("please enter an integer")


if nights < 3:
    cost = nights * trip[1][2]
    print("That will be a total of ${}".format(cost))
    total_cost = total_cost + cost
    print("The total cost of your trip now is ${}".format(total_cost))

else:
    cost = nights * trip[1][2] * 0.8
    saving = nights * trip[1][2] * 0.2
    print("That will be a total of ${}".format(cost))
    print("You just saved ${}".format(saving))
    print("")
    total_cost = total_cost + cost
    print("The total cost of your trip now is ${}".format(total_cost))
    print("")


print("We are happy to annonce that your trip is now fully booked!")
print("You will be traveling from", trip[0][0], "to",  trip[1][0])
print("and staying in", trip[1][0], "for",  nights, "nights before returning home!")
print("")
print("Thank you for using our service, we hope you have an amazing trip.")












