# Task 1) a)

"""Title : Program to print basic info 
   Use assingment & display output """ 
 
#Assign with your real info 
name = "Aqil Radzi"  
age = 21
hometown = 'Keramat Wangsa, Kuala Lumpur' 
 
#Display output 
print ('\tHave a nice day!!') 
print ('\nMy name is '+ name + '.') 
print ('I am ' + str(age) + ' years old.') 
print ('I am from ' + hometown + '.') 


# Task 1) b)

loanAmount = eval(input("\nInsert amount of loan : RM"))
interestRate = eval(input("\nInsert interest rate (%) : "))
duration = eval(input("\nInsert duration of the loan in months : "))
totalInterest = loanAmount + loanAmount*interestRate
monthlyPayment = totalInterest/duration

print("\nTotal Interest for your loan : RM" + str(totalInterest))
print("Your monthly payment : RM" + str(monthlyPayment))