from datetime import datetime
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
    #print(current_date)
    #print(valid_start_date)
    #print(valid_end_date)

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