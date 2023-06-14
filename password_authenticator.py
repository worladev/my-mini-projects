
#REDOLF
import string

# def checker():
#     var_lower_cases = string.ascii_lowercase
#     var_upper_cases = string.ascii_uppercase
#     numbers = "0123456789"
#     correct_password = "Password123"
#     user_password = input("Enter the correct password here: ") 
#     if var_lower_cases in user_password and var_upper_cases in user_password and numbers in user_password:
#         print("Let's go to the next function")

def password():
    correct_password = "Password123"
    c = 0
    while True:
        
        # global c = 0
        user_password = input("Enter the correct password here: ")
        c += 1
        if user_password == correct_password:
            print("You are logged in to the system")
            break
        if user_password != correct_password and c > 4:
            print("Your " + str(c) + " attempts are exhausted, you are kicked out!!")
            break            

#checker()
password()


# Enoch
def password():
    max_num_attempts=5
    count=0

    while count < max_num_attempts:
        password=input("Enter a password:") 
        if password=="Password123":
            print("You are logged in the system :")
            break 
        else:
            count+=1
            print("Re-enter your password: ")
    if max_num_attempts==count:
        print("You are kicked of the system ")

password()







# Coding Challenge main solution
def password_check(password):
    lower_case = 0
    upper_case = 0
    number = 0
    if len(password) >= 6:
        for char in password:
            if char.islower():
                lower_case += 1
            if char.isupper():
                upper_case += 1
            if char in "0123456789":
                number += 1
    else:
        print("password length should be more than 6")

    if (lower_case >= 1) and  (upper_case >= 1) and (number >= 1) and  (lower_case + upper_case + number) >= 6:
        return True
    else:
        return False


def password1():
    max_num_attempts=5
    count=0
    while count < max_num_attempts:
        password=input("Enter a password:") 
        if (password=="Password123") and password_check(password):
            print("You are logged in the system :")
            break 
        else:
            print("Re-enter your password: ")
        count+=1
    if max_num_attempts==count:
        print("You are kicked of the system ")

password1()




'''
CHALLENGE QUESTIONS
ENOCH 
VRS 
Abubakar

 Write a program that asks the user to enter a password. 
 If the user enters the right password,the program should 
 tell them they are logged in to the system. 
 Otherwise, the program should ask them to re-enter the password.
 The user should only get five tries to enter the password, after which point 
 the program should tell them that they are kicked off of the system.

 HINTS
 Take the user's input dynamically by asking them to enter it.
 You can write two functions: one that handles the password checking and one that checks 
 if the password is correct and displays the message accordingly.

 RULES FOR THE PASSWORD
 The password must be at least 6 characters long.
 The password must contain at least one uppercase letter (A–Z).
 The password must contain at least one lowercase letter (a–z).
 The password must contain at least one digit (0–9).
'''