def user_login(email, password):
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