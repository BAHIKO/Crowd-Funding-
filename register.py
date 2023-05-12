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

def isValidPhoneNumber(number):
  mobile_phone = number
  mobile_list = []
  for mobile in mobile_phone:
    mobile_list.append(mobile)
  return (mobile_phone.isdigit() )and (len(mobile_phone) == 11) and (mobile_list[0] == '0') and (mobile_list[1] == '1') and (mobile_list[2] == '0' or '1'or'2'or'5')