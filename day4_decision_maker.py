


#  Task1: Age Checker

print("---Welcome to the Decision Maker!---")
age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 17:
    print("You are a teenager.")
elif age >= 18 and age <= 59:
    print("You are an adult.")
else:       
    print("You are a senior citizen.") 


# Task2: Grade Checker

score = int(input("Enter your score: "))

if score > 100 or score < 0:
    print("Invalid score. Please enter a score between 0 and 100.") 
elif score >= 90:
    print("Grade: A")    
elif score >= 80:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")