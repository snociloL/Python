# Task 4 a)

countPositive = 0
countNegative = 0

value = 1

while (value <= 10):
    number = eval(input("\nPlease enter a number : "))
    if number > 0:
        countPositive+=1
    elif number < 0:
        countNegative+=1
    else:
        print("The number is zero!")
    value+=1

print("\nThe number of positive value is : " + str(countPositive))
print("The number of negative value is : " + str(countNegative))

#Task 4 b)

response = ""
quizzes = 0
n = 0
while (response != "N"):
    quizzes += eval(input("Insert marks obtain from quizzes : "))
    n += 1
    response = str(input("ADD MORE? (Y/N) : "))

print("Total amount of marks obtained : " + str(quizzes))
print("Total amount of students : " + str(n))

#Task 4 c)

vowels = 0
sentences = ""

sentences = str(input("Insert a sentence : "))

for sentence in sentences:
    if sentence.find("a") != -1 or sentence.find("A") != -1:
        vowels +=1
    elif sentence.find("e") != -1 or sentence.find("E") != -1:
        vowels +=1
    elif sentence.find("i") != -1 or sentence.find("I") != -1:
        vowels +=1
    elif sentence.find("o") != -1 or sentence.find("O") != -1:
        vowels +=1
    elif sentence.find("u") != -1 or sentence.find("U") != -1:
        vowels +=1

print("\nThere are "+ str(vowels) + " in " + sentences)