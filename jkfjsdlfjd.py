print("\nHello Rita\n")
herName = "Rita Rossweisse"

# # # We cant print both str and int/float/double at a single parameter # #

# # age = "25"
# # print("Age = " + age)



# # # Input/Scanner # #

# husbandName = input("\nWhat's the name of her husband? ")
# print("Her husband name is " + husbandName)

# birthYear = input("\nEnter her birth year = ")
# age = 2023 - int(birthYear)

# print("Her age is", age)
# myAge = 2023 - eval(input("Insert your birth year = "))
# ageDifference = age - myAge
# print("Your age difference with", herName, "is", ageDifference)    # # How to combine 2 different data types in print() # #



# # # Define Functions # #

# def loveLetter():
#     print("\nI love you, " + herName)

# loveLetter()
# print("\n", type(herName))
# print(type(age))



# # # Different kinds of basic print() methods # #

# print(hername, end="\t")
# print(herName[9])
# print(herName[-1])
# print(herName[4])
# print(len(herName))
# print(3*herName)
# print(herName[:4])
# print(herName[4:])
# print(herName)
# print(herName.upper())          #uppercase everything ( basically caps lock ON lol )
# herNameLower = herName.lower()  # lowercase everything
# print(herNameLower)
# print(herNameLower.title())     # only capitalize the first letter for each word
# print(herName.capitalize())         # only capitalize the first letter of the whole sentence/string
# print(herName.swapcase())           # basically like capitalize but NEGATIVE aka Toggle Case
# print(herName.isalnum())            #check if all char are alphanumeric
# print(herName.isalpha())            #check if all char are all alphabetic
# print(herName.isdigit())            #check if string contains numeric
# print(herName.istitle())            #check if string contains title words
# print(herName.isupper())            #check if string contains upper case
# print(herName.islower())            #check if string contains lower case
# print(herName.isspace())            #check if string contains spaces



# # String/Lists Manipulation # #

# honkaiCharas = ["Kiana", "Mei", "Bronya", "Himeko", "Fu Hua", "Durandal", "Rita Rossweisse", "Seele"]
# print(honkaiCharas)
# print(honkaiCharas[6])
# print(honkaiCharas[-6])
# print(honkaiCharas[:])
# print(honkaiCharas[3:7])
# print(honkaiCharas[0:3]*2)

# print(honkaiCharas[6].split())
# print(honkaiCharas[6].count('s'))
# print(honkaiCharas[6].startswith("R"))
# print(honkaiCharas[6].startswith("r"))
# print(honkaiCharas[6].endswith("e"))
# print(honkaiCharas[2].replace("Bronya", "Bronya Zaychik"))
# print(honkaiCharas[2])
# print("Rita Rossweisse" in honkaiCharas)

# honkaiCharas.append("Theresa")
# print(honkaiCharas)
# honkaiCharas.insert(0,"Otto")
# print(honkaiCharas)
# honkaiCharas.remove("Otto")
# print(honkaiCharas)
# honkaiCharas.extend(["Rozaliya", "Liliya"])
# print(honkaiCharas)
# del honkaiCharas[9:11]
# print(honkaiCharas)
# honkaiCharas.sort()
# print(honkaiCharas)
# honkaiCharas.reverse()
# print(honkaiCharas)

# for honkaiChara in honkaiCharas:            # printing in a column instead of a single line
#     print(honkaiChara)

# print(len(honkaiCharas))



# # # Dictionary # #

# honkaiElements = {"Physical" : "Palatinus Equinox", "Fire" : "Herrscher of Flamescion", "Ice" : "Herrscher of Reason"}
# print(honkaiElements)
# honkaiElements["Lightning"] = "Herrscher of Thunder"
# print(honkaiElements)



# # # Set # #  

ritaDataSets = {"Rita Rossweisse", "Great Britain", 1998, 25, 25}
print(ritaDataSets)                                                     # only store unique data, no duplicates
ritaDataSets.add(168)
print(ritaDataSets)
ritaAccurateDataSets = {"Rita Rossweisse", "Great Britain", 1998, 25, 56, 168}
ritaDataSets.update(ritaAccurateDataSets)
print(ritaDataSets)
ritaDataSets.discard(56)
print(ritaDataSets)

for ritaDataSet in ritaDataSets:
    print(ritaDataSet)

honkaiHerrschers = {"Herrscher of Flamescion", "Herrscher of Reason", "Herrshcer of Thunder"}
honkaiHerrscherss = {"Herrscher of Finality",  "Herrscher of Truth", "Herrscher of Origin"}
print(honkaiHerrschers | honkaiHerrscherss)             # OR print(honkaiHerrschers.union(honkaiHerrscherss))