# Task 2 a)

age = 24 
print ("Guess my age, you have 1 chance!") 
guess = int (input ("Guess: ")) 
if guess != age: 
    print ("Wrong!") 
else: 
    print ("Correct") 

# Task 2 b)
salutation = " "
name = str(input("\nInsert your name : "))
gender = str(input("Insert your gender (M/F) : "))
maritalStatus = str(input("Insert your marital status (Single/Married/Divorced/Cheated) : "))

if gender == 'M':
    salutation = "Mr "
elif (gender == 'F' and maritalStatus == "Single"):
    salutation = "Miss "
elif (gender == 'F' and maritalStatus == "Married"):
    salutation = "Mrs "

print("\nWelcome " + salutation + name)

# Task 2 c)

### Program to calculate parking charge ### 
 
typeVehicle = input("Enter vehicle type (C-car/B-bus/T-truck): ") 
# hourSpent = ____________________i)  
hourSpent = eval(input("Enter parking hour(s) spent : "))

if typeVehicle == 'c' or typeVehicle == 'C': 
    vehicle = 'Car' 
    rate = 2.0 
# elif ____________________ii) 
elif typeVehicle == 'b' or typeVehicle == 'B':

    vehicle = 'Bus' 
    rate = 3.0 
elif typeVehicle == 't' or typeVehicle == 'T': 
    vehicle = 'Truck' 
    rate = 4.0 
else: 
    rate = 0.0 
# parkingCharge = ____________________iii) 
parkingCharge = rate*hourSpent

print ("Vehicle Type : "+ typeVehicle) 
print ("Hours Spent : "+ str(hourSpent))
# print ____________________iv
print("Total parking charges : RM" + str(parkingCharge))

# Task 3

roomType = str(input("\nInsert Room Type (Standard/Family) : "))
bedType = str(input("\nInsert Bed Type (Single/Double) : "))
ratePerNight = 0.0

if roomType == "Standard":
    if bedType == "Single":
        ratePerNight = 80.0
    elif bedType == "Double":
        ratePerNight = 120.0
elif roomType == "Family":
    if bedType == "Single":
        ratePerNight = 110.0
    elif bedType == "Double":
        ratePerNight = 160.0

custName = str(input("\nInsert Customer Name : "))
custID = str(input("\nInsert Customer ID : "))
phoneNum = str(input("\nInsert Phone Number : "))
daysOfStay = int(input("\nInsert Day(s) of Stay : "))

totalFee = ratePerNight*daysOfStay
print("\nCustomer Details :-")
print("\nCustomer Name : "+custName)
print("Customer ID : "+custID)
print("Customer Phone Number : "+phoneNum)
print("Room Details : "+roomType + " " + bedType)

print("\nTotal fee of stay : RM" + str(totalFee))