print("Hello Rita")

# age = "25"
# print("Age = " + age)

husbandName = input("\nWhat's the name of her husband? ")
print("Her husband name is " + husbandName)

birthYear = input("\nEnter her birth year = ")
age = 2023 - int(birthYear)
print("Her age is", age)

herName = "Rita Rossweisse"

def loveLetter():
    print("\nI love you, " + herName)

loveLetter()

print("\n", type(herName))
print(type(age))