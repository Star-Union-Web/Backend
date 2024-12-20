import json
from inputHandler import *

command = ""
menu = 0
tasks_list = []

with open("tasks.json", "r") as f:
  tasks_list=json.load(f)
f.close()

print("Please Choose Preferred Action: ")
print("1.Add Task\n2.List Tasks\n3.Modify Task\n4.Delete Task\n5.Exit")

while command != "5":
  command = input(">:")

  if menu == 0:
    if command == "1":

      desc = input("Task Description: ")
      deadline = handle_date(input("Ente Due Date (YYY/MMM/DDD, HH:MM): "))
      priority = handle_priority(int(input("Enter Priority (1, 2, 3): ")))
      
      tasks_list.append({"desc": desc, "deadline": deadline, "priority": priority})
      
    elif command == "2":
      for i in range(len(tasks_list)):
        print(f"{i+1}. {tasks_list[i]["desc"]}\n\nDeadline: {tasks_list[i]["deadline"]}\n\nPriority: {tasks_list[i]["priority"]}\n")
        print("-----------------------------------------------------\n")
    elif command == "3":
      if len(tasks_list) != 0:
        task_id = int(input("Enter Task ID to Modify: "))
        task_id = handleIdx(task_id, len(tasks_list))
        print(f"1. {tasks_list[task_id-1]["desc"]}\n\n2. Deadline: {tasks_list[task_id-1]["deadline"]}\n\n3. Priority: {tasks_list[task_id-1]["priority"]}\n")
        tasks_list[task_id-1]["desc"] = input("Task Description: ")
        tasks_list[task_id-1]["deadline"] = handle_date(input("Ente Due Date (YYY/MMM/DDD, HH:MM): "))
        tasks_list[task_id-1]["priority"] = handle_priority(int(input("Enter Priority (1, 2, 3): ")))

      else:
        print("Nothing To Edit")


    elif command == "4":
      if len(tasks_list) != 0:
        task_id = int(input("Enter Task ID to Delete: "))
        task_id = handleIdx(task_id, len(tasks_list))
        del tasks_list[task_id-1]
        
      else:
        print("Nothing to Delete")

    with open("tasks.json", "w") as f:
      f.write(json.dumps(tasks_list))
    f.close()
