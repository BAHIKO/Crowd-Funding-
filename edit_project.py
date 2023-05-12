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
