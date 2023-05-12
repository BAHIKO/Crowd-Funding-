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