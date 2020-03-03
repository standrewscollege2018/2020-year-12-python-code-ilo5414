#travel company program
#this program will calculate the total cost of a customers holiday from flights to accomodation costs

departure = [["Auckland", 0], ["Wellington", 50], ["Christchurch", 75]]
destination = [["Sydney", 326, 120], ["Tonga", 378, 40], ["Shanghai", 1436, 60], ["London", 2376, 80]]
total_cost = 0

print("Welcome to Logie's Legendary travel service!")
print("We are so happy we can help you today")
print("")

print("Lets get your flights sorted!")
print("Where will you be departing New Zealand from?")
print("")

for index in range(0, len(departure)):
    print("{}. {} - connecting flight cost: ${}" .format(index+1, departure[index][0], departure[index][1]))

