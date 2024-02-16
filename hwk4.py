import random
import string
def gen():
    """ Creates and returns a random generated Username """
    first =["John","Robert","Paul","Roblox","Roblox2"]
    last = ["William","Copert","Gold","Lion","Forens"]
    gen_name = random.choice(last)+" "+random.choice(first)
    return gen_name
def gen_pass():
    """ creates a random password for the user """
    #Makes it so all the chars are lowercase
    
    s = string.ascii_lowercase
    #Generates a random lowercase char 8 times
    passw = ''.join(random.choice(s) for i in range(8))
    return passw
def birth():
    """ Creates and returns a random generated birthdate"""
    day = ""
    #Generates a random date seperated by /s
    day = day + str(random.randint(1,12)) + "/" + str(random.randint(1,31)) + "/" + str(random.randint(1900,2024))
    return day
def address():
    """Creates a random address """
    home = ""
    #Generate a random 5 digit home number
    home = ''.join(str(random.randint(0,9)) for i in range(5))
    #Create a some street, city, and state names
    street = ["Cass","Panama","Cunningham","Mays","Tibieth","WonderWorld"]
    city = ["Warren","Detroit","NewYork","Dearborn","Mordor"]
    state = ["MI","NY"]
    home = home + random.choice(street) + " " + random.choice(city) + " " + random.choice(state)
    return home
def ssn():
    """ Creates a random social security number """
    num = ""
    num = ''.join(str(random.randint(0,9)) for i in range(3))
    num += "-"
    num += ''.join(str(random.randint(0,9)) for i in range(2))
    num += "-"
    num += ''.join(str(random.randint(0,9)) for i in range(4))
    return num
def product():
    """ Creates a random product purchased """
    stuff = ["Water Bottle","Beyblade","Pen","Pencil","TV","Laptop","2004 Honda Civic","Kangaroo","iphone 6"]
    prod = random.choice(stuff)
    return prod
def sales():
    """ Creates a random sales person"""
    person = ["John Smith","Robert William","Old Man","Wizard of Oz","Bruce Wayne","Clark Kent"]
    sale_person = random.choice(person)
    return sale_person
def key():
    """ Creates a unique key """
    ID = ''.join(str(random.randint(0,9)) for i in range(10))
    return ID
#Create a list to hold the employees
employee_list = []
#Creates 20 people and puts them in the list
for i in range(20):
    employee_list.append([key(),gen(),gen_pass(),birth(),address(),ssn(),product(),sales()])
    
# Print the employee information in a neat format
for employee in employee_list:
    print("ID:", employee[0])
    print("Name:", employee[1])
    print("Password:", employee[2])
    print("Birthdate:", employee[3])
    print("Address:", employee[4])
    print("SSN:", employee[5])
    print("Product Purchased:", employee[6])
    print("Sales Person:", employee[7])
    print()  # Add an empty line for better readability between employees
#Creation of a basic menu that will search and print the person
x = 0
while(x == 0):
    choice = input("Enter the ID of the person you wish to search, else press 0 and return to screen: ")
    if(choice == 0):
        x += 1
    else:
        found = False
        for employee in employee_list:
            if choice == employee[0]:
                found = True
                print("Employee Information:")
                print("ID:", employee[0])
                print("Name:", employee[1])
                print("Password:", employee[2])
                print("Birthdate:", employee[3])
                print("Address:", employee[4])
                print("SSN:", employee[5])
                print("Product Purchased:", employee[6])
                print("Sales Person:", employee[7])
                break  # Stop searching once the ID is found
        if not found:
            print("Employee with ID {} not found.".format(choice))
