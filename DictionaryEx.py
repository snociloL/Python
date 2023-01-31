# Task 1 a) BMI

StudentBMI = []
student = {}
counter = 0
def countOverweight(bmi):
    global counter
    if bmi > 25.0:
        counter += 1
def updateComment(bmi):
    comment = ''
    if bmi < 18.5:
        comment = 'UNDERWEIGHT'
    elif bmi >= 18.5 and bmi <= 25.0:
        comment = 'NORMAL'
    elif bmi > 25.0:
        comment = 'OVERWEIGHT'
    return comment

totalStudent = int(input("Enter number of student : "))
for i in range(totalStudent):
    name = input('\nEnter student name : ')
    h = float(input('Enter student height (in meter) : '))
    w = float(input('Enter student weight (in kilogram) : '))
    bmi = w/(h*h)
    print('BMI = ', bmi)
    # create dictionary for student info
    
    student = {'name':name, 'height':h, 'weight':w, 'bmi': round(bmi, 2), 'comment' : updateComment(bmi)}
    StudentBMI.append(student) # Store student info into list

# display all student bmo record 
print('\nList of student for BMI Records :- ')

for stud in StudentBMI:
    print(stud)

# display all student name and bmi value
print('\nList of Student (Name & BMI Value) :-')

for record in StudentBMI:
    print(record['name'],"\t",record['bmi'],"\t",record['comment'])
    countOverweight(record['bmi'])

print("Total of OVERWEIGHT students : ", counter)


# Task 2

# class BMI:
#     def __init__(self, h, w, name):
#         self.h = h
#         self.w = w
#         self.name = name        

#     def caclBMI():
#         bmi = w/(h*h)
#         return bmi

#     def StudentList(): 
#         student = {'name':name, 'height':h, 'weight':w, 'bmi': round(bmi, 2)}


# Task 3

participantType = '' #Students/Staffs/Outsiders
participantCode = '' # T/S/O
itemCode = '' # W/D
charges = 0.0
totalCanopies = 0
day = 0

def canopyCharges(participantCode, totalCanopies, day):
    global charges
    if participantCode == 'T':
        charges = 90.0
    elif participantCode == 'S':
        charges = 150.0
    elif participantCode == 'O':
        charges = 200.0
    return charges*totalCanopies*day

def additionalCharges(itemCode):
    global charges
    if itemCode == 'W':
        charges = 100.0
    else:
        charges = 0.0
    return charges

total = 0
request = ''
print("\n\tWelcome to The Entreprenuer Club ")
while (request != "No"):
    participantCode = str(input("\nPlease insert participant code (T/S/O) :"))
    totalCanopies = int(input("\nPlease insert number of canopies :"))
    day = int(input("\nPlease insert total days of rental :"))
    itemCode = str(input("\nPlease insert item code (D/W):"))
    total = canopyCharges(participantCode, totalCanopies, day) + additionalCharges(itemCode)
    print("\n\t Total of Charges : RM", total)
    request = str(input("\n\nContinue program? (Yes/No) : "))