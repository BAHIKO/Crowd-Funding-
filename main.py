import sys
from edit_project import edit_project
from login import user_login
from register import user_register
from register import isValidPhoneNumber
from create_project import create_project
from view_project import view_projects
from delete_project import delete_project
from search import search_projects




# End of helper functions

#  start of Auth
user_choice = input("Do you have an existing account? (Y/N)")

user = None

# login
if user_choice.upper() == "Y":
  email = input("Enter your email: ")
  password = input("Enter your password: ")
  user = user_login(email, password)

  if (not user):
    print("Login Failed")
    sys.exit()

# register
elif user_choice.upper() == "N":
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  email = input("Enter your email: ")
  password = input("Enter your password: ")
  confirm_password = input("Confirm your password: ")
  mobile_phone = input("Enter your mobile phone number: ")
  user = user_register(first_name, last_name, email, password,
                       confirm_password, mobile_phone)
else:
  print("Invalid Input!")
  sys.exit(0)
#  End of Auth

while (True):
  # create project
  # view projects
  # edit project
  # delete project

  print("For Create Project enter 1")
  print("For view Project enter 2: ")
  print("For edit Project enter 3: ")
  print("For delete Project enter 4: ")
  print("For search for Project enter 5: ")
  print("For Exit press 0: ")

  user_choice = input("Enter command: ")

  if (user_choice == "0"):
    sys.exit(0)
  if (user_choice == "1"):
    create_project(user)
  elif (user_choice == "2"):
    view_projects(user)
  elif (user_choice == "3"):
    edit_project(user)
  elif (user_choice == "4"):
    delete_project(user)
  elif (user_choice =="5"):
    search_projects(user)
