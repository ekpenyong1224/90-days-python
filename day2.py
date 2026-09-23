#Day 2 -My Bio Data Program
print("---My Bio---")
full_name = input("Enter your full name:")
age = int(input("Enter your age:"))
city = input("Enter your city:")
best_language = input("Your favorite programming language:")
years_to_90 = 90 - age

print(f"\nHello {full_name}!")
print(f"You are {age} years old and you live in {city}.")
print(f"Your favorite programming language is {best_language}.")
print(f"You have {years_to_90} years left to reach 90.")
print(f"Your name has {len(full_name)} characters.")# len() function is used to count the number of characters in the string.


# check type of the variable
print(f"\nType of age is: {type(age)}")
print(f"Type of city is: {type(city)}")
print(f"Type of best_language is: {type(best_language)}")   
