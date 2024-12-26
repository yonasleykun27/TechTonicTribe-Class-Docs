#write full name of a person

# first_name="Yonas"
# last_name="Leykun"
# full_name=first_name+" "+last_name
# print ("Full Name: ", full_name)

#age 
# age= int(input("enter the number "))
# if age >=18:
#     print ("you are adult")     
# else:
#     print ("you are minor.")

# #swap
# a,b,c = 1,2,3
# # a = int(input("enter first  number "))
# # b = int(input("enter second number "))
# # c = int(input("enter third number "))
# print ("before swap", a,b,c)
# a,b,c = c,b,a
# print ("after swap", a,b,c)


# #swap by name 

# first_name= (input("enter your first name "))
# last_name= (input("enter your last name "))

# print ("before swap:", first_name,last_name)
# first_name, last_name = last_name, first_name
# print ("after swap:", first_name,last_name)

# PWD CHECKER

# def get_saved_wifi_passwords():
#     try:
#         # Get the list of WiFi profiles
#         profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True, encoding='utf-8')
        
#         # Extract WiFi profile names
#         profiles = [line.split(":")[1].strip() for line in profiles_data.split("\n") if "All User Profile" in line]
        
#         wifi_passwords = {}
#         for profile in profiles:
#             try:
#                 # Get the WiFi password for each profile
#                 profile_info = subprocess.check_output(f"netsh wlan show profile name=\"{profile}\" key=clear", shell=True, encoding='utf-8')
#                 # Find the line with the password
#                 password_line = [line for line in profile_info.split("\n") if "Key Content" in line]
#                 if password_line:
#                     # Extract the password
#                     password = password_line[0].split(":")[1].strip()
#                 else:
#                     password = None  # No password stored
#                 wifi_passwords[profile] = password
#             except subprocess.CalledProcessError:
#                 wifi_passwords[profile] = None
        
#         return wifi_passwords
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return {}

# if __name__ == "__main__":
#     wifi_passwords = get_saved_wifi_passwords()
#     if wifi_passwords:
#         print("Saved WiFi Passwords:")
#         for wifi, password in wifi_passwords.items():
#             print(f"{wifi}: {password if password else 'No password saved'}")
#     else:
#         print("No WiFi profiles found or an error occurred.")

# #question 1
# x= int(input("enter the number: "))
# if x>0:
#     print("positive")
# elif x<0:
#     print("negative")
# else:
#     print("neither")

# #question 2
# age= int(input("enter the number "))
# if age >=18:
#     print ("you can vote")     
# else:
#     print ("you can't vote for now ")

# #question 3

# a = int(input("enter first  number "))
# b = int(input("enter second number "))

# if a>b: 
#     print(a)
# else:
#     print(b)

# #try to check with 3 numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b and a > c: 
#     print("The largest number is:", a)
# elif b > c: 
#     print("The largest number is:", b)
# else:  
#     print("The largest number is:", c)


# # yab
# attendance=float(input("enter the no"))
# score=float(input("enter the no"))
# if attendance>=75:
#     print ("you can check")
#     if score>=50:
#         print("you passed ")
#     else:
#         print ("you failed ")
# else:
#     print ("you failed by low attendance")


# yon code

# attendance = int(input("enter the number of attend? "))
# score  = int(input("enter the score? "))

# if attendance >= 75:
#         if score>= 50:
#                 print("You passed the course")
#         else:
#                 print("You failed the course")
# else:
#         print("You failed the course due to low attendance")

# #write a python program that uses  a for loop calculate the sum of all even number

# #steps to follow 
# #use a for loop to iterate through the numbers form 1 to 20.


# sum=0
# for i in range(21):
#     sum=sum+i
#     print(sum)

# #check if each number is even

# sum=0
# for i in range(21):
#     sum=sum+i
#     print(sum)


# check this question
# num = int(input("enter the num? "))

# if num / 5:
#         print(num)
# elif num / 2:
#          print(num)      
#         else:
#                 print("not ")
# else:
#         print("You failed the course due to low attendance")

