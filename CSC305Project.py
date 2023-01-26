# Need to implement concept of List and function
# Data Dictionary

foodLists = {'Tom Yunk Campur': 12.9, 'Siakap 2+1 Rasa' : 27.5, 'Ikan Merapu Stim Aq' : 30.0, 'Mee Goreng Ayum' : 7.8, 'Udang Goreng Tepunk': 6.0,}
for foodList in foodLists:
    print(foodList)

profit = 0.00
response = 1

while (response != 4):
    print("\n\t~~~~~~~~~~~~~~~~~~~~~ Menu Page ~~~~~~~~~~~~~~~~~~~~~")
    print("\n\t Command Codes : \n\t(1) Order - To set a customer order. \n\t(2) Profit - To check total earnings. \n\t(3) Top - To see customer's favorite order and all menu. \n\t(4) To exit.")
    response = eval(input("\n\tInput = "))

    if response == 1:
        print("\t\nCustomer Order(s) : -")
        print("\t================================================================")
    elif response == 2:
        print("\n\t~~~~~~~~~~~~~~~~~~~~~ Current Profit ~~~~~~~~~~~~~~~~~~~~~")
        print("\tTotal profits : RM"+str(profit))
    elif response == 3:
        print("\n\t~~~~~~~~~~~~~~~~~~~~~ Top favorite orders ~~~~~~~~~~~~~~~~~~~~")
        print("\tIkan Merapu Stim Aq = RM30.00")
        print("\n\t~~~~~~~~~~~~~~~~~~~~~ All Menu ~~~~~~~~~~~~~~~~~~~~")
        for foodList in foodLists:
            print("\t"+ foodList)

    elif response == 4:
        print("\n\t~~~~~~~~~~~~~~~~~~~~~ Thank you for the hard work ~~~~~~~~~~~~~~~~~~~~")
    else:
        print("ERROR!! Unknown Command")
