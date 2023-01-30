# Need to implement concept of List and function
# Data Dictionary


foodLists = {'Tom Yunk Campur': 12.9, 'Siakap 2+1 Rasa' : 27.5, 'Ikan Merapu Stim Aq' : 30.0, 'Mee Goreng Ayum' : 7.8, 'Udang Goreng Tepunk': 6.0}
drinkLists = ['Pen Pineapple Apple Juice', 'Soy Bean Milk','Aiyar Ping', 'Chocola Milk', 'Fresh Milk']
def printMenu():
    for foodList in foodLists:
            print("\t"+ foodList, foodLists.get(foodList))
    drinkLists.sort()
    for drinkList in drinkLists:
            print("\t"+ drinkList)

def calcTotalOrder():
    total = 0.0
    for prices in price:
            total = total +prices
    return total

def printOrder():
    for listOrders in listOrder:
        print("\t"+ listOrders)
price = []
listOrder = []
def orderMenu(code):
        if code == 1:
           listOrder.append("Tom Yunk Campur  RM 12.90")
           print("\tTom Yunk Campur  RM 12.90")
           price.append(12.9)
        elif code == 2:
            listOrder.append("Siakap 2+1 Rasa  RM 27.50")
            print("\tSiakap 2+1 Rasa  RM 27.50")
            price.append(27.5)
        elif code == 3:
            listOrder.append("Ikan Merapu Stim Aq  RM 30.00")
            print("\tIkan Merapu Stim Aq  RM 30.00")
            price.append(30.0)
        elif code == 4:
            listOrder.append("Nasi Goreng Ayum  RM 7.80")
            print("\tNasi Goreng Ayum  RM 7.80")
            price.append(7.8)
        elif code == 5:
            listOrder.append("Udang Goreng Tepunk  RM 6.00")
            print("\tUdang Goreng Tepunk  RM 6.00")
            price.append(6.0)
        elif code == 6:
            listOrder.append("Aiyar Ping  RM 2.90")
            print("\tAiyar Ping  RM 2.90")
            price.append(2.9)
        elif code == 7:
            listOrder.append("Chocola Milk  RM 7.50")
            print("\tChocola Milk  RM 7.50")
            price.append(7.5)
        elif code == 8:
            listOrder.append("Fresh Milk  RM 3.00")
            print("\tFresh Milk  RM 3.00")
            price.append(3.0)
        elif code == 9:
            listOrder.append("Pen Pineapple Apple Juice  RM 5.00")
            print("\tPen Pineapple Apple Juice  RM 5.00")
            price.append(5.0)
        elif code == 10:
            listOrder.append("Soy Bean Milk  RM 5.00")
            print("\tSoy Bean Milk  RM 5.00")
            price.append(5.0)
        else:
            print("\tWrong Input!!")

def main():
    tableNum = 0
    profit = 0.00
    response = 0
    confirm = ""
    loop = ""
    while (response != 4):
        print("\n\t~~~~~~~~~~~~~~~~~~~~~ Menu Page ~~~~~~~~~~~~~~~~~~~~~")
        print("\n\t Command Codes : \n\t(1) Order - To set a customer order. \n\t(2) Profit - To check total earnings. \n\t(3) Top - To see customer's favorite order and all menu. \n\t(4) To exit.")
        response = eval(input("\n\tInput = "))

        if response == 1:
            print("\t\nCustomer Order(s) : -")
            print("\t================================================================")   
            tableNum = int(input("\n\t Insert table number = "))
            while(loop != "No"):
                code = eval(input("\n\tInsert item code = "))
                orderMenu(code)
                loop = str(input("\tAdd another order? (Yes/No) = "))
                
            confirm = str(input("\tConfirm Order? (Yes/No) = "))
            if(confirm == "No"):
                listOrder.clear()
                total = 0.0

            print("\n\tTable Number = ", tableNum)
            print("\n\tList of order = ")
            printOrder()
            total = calcTotalOrder()
            profit = profit + total
            print("\n\tTotal of order = RM", total)

        elif response == 2:
            print("\n\t~~~~~~~~~~~~~~~~~~~~~ Current Profit ~~~~~~~~~~~~~~~~~~~~~")
            print("\tTotal profits : RM"+str(profit))
        elif response == 3:
            print("\n\t~~~~~~~~~~~~~~~~~~~~~ Signature Menu ~~~~~~~~~~~~~~~~~~~~")
            print("\tIkan Merapu Stim Aq = RM30.00")
            print("\n\t~~~~~~~~~~~~~~~~~~~~~ All Menu ~~~~~~~~~~~~~~~~~~~~")
            printMenu()

        elif response == 4:
            print("\n\t~~~~~~~~~~~~~~~~~~~~~ Thank you for the hard work ~~~~~~~~~~~~~~~~~~~~")
        else:
            print("ERROR!! Unknown Command")

main()