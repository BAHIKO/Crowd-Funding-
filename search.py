from datetime import datetime

def search_projects(user):
    c = int(
        input("Choose the way you want to search:\n1. By title\n2. By details\n3. By total target\n4. By start date\n"))

    if c == 1:
        t = input("Enter the title: ")
        with open("projects.txt", "r") as file:
            lines = file.readlines()
            for project_line in lines:
                data = project_line.split(":")
                if t == data[1]:
                    print("Title:", data[2])
                    print("Details:", data[2])
                    print("Total Target:", data[3])
                    print("Start Time:", data[4])
                    print("End Time:", data[5])

    elif c == 2:
        d = input("Enter the details: ")
        with open("projects.txt", "r") as file:
            lines = file.readlines()
            for project_line in lines:
                data = project_line.split(":")
                if d == data[2]:
                    print("Title:", data[2])
                    print("Details:", data[2])
                    print("Total Target:", data[3])
                    print("Start Time:", data[4])
                    print("End Time:", data[5])



