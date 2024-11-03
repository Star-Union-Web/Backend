import json
from tasks import Task
from inputHandler import *

t1 = Task(1, 2, "123e", 1)

print(t1.desc)



command = ""
menu = 0
ds = []

with open("tasks.json", "r") as f:
  for line in f:
    ds = json.loads(line)
f.close()
print("Please Choose Preferred Action: ")
print("1.Add Task\n2.List Tasks\n3.Modify Task\n4.Delete Task\n5.Exit")
while command != "5":
  command = input(">:")
  if menu == 0:
    if command == "1":

      desc = input("Task Description: ")
      deadline = handleDate(input("Ente Due Date (YYY/MMM/DDD, HH:MM): "))
      priority = handlePriority(int(input("Enter Priority (1, 2, 3): ")))
      
      ds.append({"desc": desc, "deadline": deadline, "priority": priority})
      
    elif command == "2":
      for i in range(len(ds)):
        print(f"{i+1}. {ds[i]["desc"]}\n\nDeadline: {ds[i]["deadline"]}\n\nPriority: {ds[i]["priority"]}\n")
        print("-----------------------------------------------------\n")
    elif command == "3":
      

      if len(ds) != 0:
        taskId = int(input("Enter Task ID to Modify: "))
        taskId = handleIdx(taskId, len(ds))
        print(f"1. {ds[taskId-1]["desc"]}\n\n2. Deadline: {ds[taskId-1]["deadline"]}\n\n3. Priority: {ds[taskId-1]["priority"]}\n")
        ds[taskId-1]["desc"] = input("Task Description: ")
        ds[taskId-1]["deadline"] = handleDate(input("Ente Due Date (YYY/MMM/DDD, HH:MM): "))
        ds[taskId-1]["priority"] = handlePriority(int(input("Enter Priority (1, 2, 3): ")))
      else:
        print("Nothing To Edit")

    elif command == "4":
      if len(ds) != 0:
        taskId = int(input("Enter Task ID to Delete: "))
        taskId = handleIdx(taskId, len(ds))
        del ds[taskId-1]
      else:
        print("Nothing to Delete")

    with open("tasks.json", "w") as f:
      f.write(json.dumps(ds))
    f.close()
