import sys
from datetime import datetime
import re


#  Start of Helper Functions
def user_login(emil, pasaword):
  file = open("users.txt", "r")
  lines = file.readlines()
  for user in lines:
    data = user.split(":")
    if data[2] == email and data[3] == password:
      print(f"\nwelcome {data[0]}")
      lines.remove(user)
      return {
        "first_name": data[0],
        "last_name": data[1],
        "email": data[2],
        "password": data[3],
        "mobile_phone": data[4].strip("\n")
      }


def user_register(first_name, last_name, email, password, confirm_password,
                  mobile_phone):
  if password != confirm_password:
    print("Passwords do not match. Please try again.")
  elif not isValidPhoneNumber(mobile_phone):
    print("Invalid phone number. Please enter a valid Egyptian phone number.")
    sys.exit(0);
  else:
    line = f"{first_name}:{last_name}:{email}:{password}:{mobile_phone}\n"
    file = open("users.txt", "a")
    file.writelines(line)
    file.close()
    data = {
      "first_name": first_name,
      "last_name": last_name,
      "email": email,
      "password": password,
      "mobile_phone": mobile_phone
    }
    return data


def create_project(user):
  title = input("Enter your title: ")
  details = input("Enter your details: ")
  total_target = input("Enter your total target: ")
  start_time = input("Enter your total start time (dd/mm/yyyy): ")
  end_time = input("Enter your total end time (dd/mm/yyyy): ")

  try:
    valid_start_date = datetime.strptime(start_time, '%m/%d/%Y')
    valid_end_date = datetime.strptime(end_time, '%m/%d/%Y')
    current_date = datetime.today()

    if(valid_start_date < current_date):
      print("start date should on future")
      return
    if(valid_end_date < valid_start_date):
      print("end date should on future")
      return
  except ValueError:
    print('Invalid date!')
    return

  user_email = user["email"]

  line = f"{user_email}:{title}:{details}:{total_target}:{start_time}:{end_time}\n"
  file = open("projects.txt", "a")
  file.writelines(line)
  file.close()
  project = {
    "title": title,
    "details": details,
    "total_target": total_target,
    "start_time": start_time,
    "end_time": end_time
  }

  print("\nProject Create Successfully")
  return project


def view_projects(user):
  file = open("projects.txt", "r")
  lines = file.readlines()

  # loop over projects
  for project_line in lines:
    data = project_line.split(":")

    # check if project is owned by current user
    user_email = user["email"]
    if data[0] == user_email:
      print("title", data[1])
      print("details", data[2])
      print("total_target", data[3])
      print("start_time", data[4])
      print("end_time", data[5])
      print_line()


def delete_project(user):
  project_title = input("Please Enter Project title to delete:")
  project_found = False
  user_email = user["email"]

  # read all lines
  with open("projects.txt", "r") as f:
    lines = f.readlines()
  # write all lines again expect the one with required title
  with open("projects.txt", "w") as f:
    for line in lines:
      data = line.split(":")
      if data[1] == project_title and data[0] == user_email:
        project_found = True
      else:
        f.write(line)

  if (not project_found):
    print("Did not find Project with this tilte ", project_title)
  else:
    print("Project Deleted Successfully")


def edit_project(user):
  project_title = input("Please Enter Project title to edit:")
  project_found = False
  user_email = user["email"]

  # read all lines
  with open("projects.txt", "r") as f:
    lines = f.readlines()
  # write all lines again expect the one with required title
  with open("projects.txt", "w") as f:
    for line in lines:
      data = line.split(":")
      if data[1] == project_title and data[0] == user_email:
        project_found = True
        title = input("Enter your new title: ")
        details = input("Enter your new details: ")
        total_target = input("Enter your new total target: ")
        start_time = input("Enter your new total start time (dd-mm-yyyy): ")
        end_time = input("Enter your new total end time (dd-mm-yyyy): ")

        user_email = user["email"]

        line = f"{user_email}:{title}:{details}:{total_target}:{start_time}:{end_time}\n"
        f.write(line)

        print("\nProject edited Successfully")
      else:
        f.write(line)

  if (not project_found):
    print("Did not find Project with this tilte ", project_title)


def isValidPhoneNumber(number):
  mobile_phone = number
  mobile_list = []
  for mobile in mobile_phone:
    mobile_list.append(mobile)
  return mobile_phone.isdigit() and len(mobile_phone) == 11 and mobile_list[0] == '0' and mobile_list[1] == '1' and mobile_list[2] == '0' or '1'or'2'or'5'



def print_line():
  print("")
  print("")


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
  print_line()
  print("For Create Project enter 1")
  print("For view Project enter 2: ")
  print("For edit Project enter 3: ")
  print("For delete Project enter 4: ")
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
