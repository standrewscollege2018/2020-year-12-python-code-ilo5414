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
print("Total cost of your trip so far..",  total_cost)
#displaying where they are departing from
print("Looks like you are departing from..")
print(trip[0][0])
print("")

#destination section
print("Time to select your destination!")
print("please select one of the following destinations")
print("")
#displaying the destination options and flight costs 
for index in range(0, len(destination)):
    print("{}. {} - connecting flight cost: ${}" .format(index+1, destination[index][0], destination[index][1]))


    


