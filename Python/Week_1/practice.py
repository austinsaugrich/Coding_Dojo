"""
Specifications
    Accept an input from the user
    Determine the persons grade or that they are an adult
        If the person is over 18, they are considered an adult
        If the person is older than 3 but younger than 6, they are in preschool.
        The person is in high school if they are 14 or older, but not yet an adult.
        If the person is older than 10, and not in high school, they are in middle school.
        If the person is less than 4 years old, they are an infant.
        The remaining ages are in grade school.

    Print the result
        “The person is 14 years old and in high school.”
        “The person is 30 years old and an adult”
        "the person is 5 years old and in preschool"
        “The person is 3 years old and an infant”
        "The person is 11 years old and in middle school"
        "The person is 7 years old and in grade school"

"""
is_active = True

while is_active:

    user_input = input("Age: ")
    
    if user_input == "quit":
        is_active = False
        continue

    age = int(user_input)
   
    if age > 18:
        print(f"The person is {age} years old and an adult.")
    elif age >= 14 and age <= 18:
        print(f"The person is {age} years old and in highschool.")
    elif age > 3 and age < 6:
        print(f"The person is {age} years old and in preschool.")
    elif age < 4:
        print(f"The person is {age} years old and an infant.")
    elif age > 10 and age < 14:
        print(f"The person is {age} years old and in middleschool.")
    elif age >= 7 and age <= 10:
        print(f"The person is {age} years old and in gradeschool.")
    else:
        print("Have A Nice Day!")