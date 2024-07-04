"""Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password.  

"""
import re #importing the regex libarary to perform string matching

feedback = []
def check_password_strength(password):

    Lower_Case=r"(?=.*[a-z])" #check for lower case match
    Upper_Case=r"^(?=.*[A-Z])" #check for upper case match
    Numbers=r"^(?=.*[0-9])" #check for number match
    spc_char=r"(?=.*[!@#$&])" #check for special character !,@,#,$,&
    all_check=r"[A-Za-z\d!@#$&]{8,}$" #check if the count of characters is more than 8 including the all the above requirements

    strength = re.compile((Lower_Case)+(Upper_Case)+(Numbers)+(spc_char)+(all_check))
    if re.search(strength, password):
        return True
    else:
        if len(password)<8:
            feedback.append("Password length is less than 8 characters")
        if not re.findall(r"\d",password):
            feedback.append("Digit is missing")
        if not re.findall(r"[a-z]",password):
            feedback.append("Lower case letter is missing")
        if not re.findall(r"[A-Z]",password):
            feedback.append("Upper case letter is missing")
        if not re.findall(r"[!@#$&]",password):
            feedback.append("Special character is missing eg !, @, #, $, &")
            return False
        
while True:
        
    password = input("Enter your password : ")

    if check_password_strength(password): #calling the check function
        print("Password strength is good!")
        break
    else:

        print("Password strength is bad! \n")
        print("These are feedbacks! Please change your password accordingly")
        i=1
        for f in feedback:
            print(i, ". ", f, "\n") #printing what was not present in the password from the list
            i = i+1
        print("Retry!")

    