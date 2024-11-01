import math

tasks = []

class Task:
    def __init__(self, name, deadline=math.inf):
        self.name = name
        self.deadline = deadline
        self.done = False

    def print(self):
        print(f"{self.name}")
        print(f"Deadline: {self.deadline}")
        print(f"Done: {self.done}")

    def complete_task(self):
        self.done = True


def add_task(name, deadline):
    tasks.append(Task(name, deadline))


def complete_task(task_idx):
    if task_idx < len(tasks):
        tasks[task_idx].complete_task()
    else:
        print("Invalid task index")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")

    for i, task in enumerate(tasks):
        print(f"{i+1}", end=". ")
        task.print()
        print("-"*20)


def delete_task(task_idx):
    if task_idx < len(tasks):
        task_name = tasks[task_idx].name
        del tasks[task_idx]
        return task_name
    else:
        print("Invalid task index")


def add_task_interface():
    task_name = input("Enter task name: ")
    deadline = int(input("Enter days left to deadline: "))

    add_task(task_name, deadline)

    print ("Task added successfuly!")


def delete_task_interface():
    task_id = int(input("Enter task id: "))
    name = delete_task(task_id)

    print(f"Task ({name}) deleted succcessfuly!")

if __name__ == "__main__":

    print("Task manager")
    print("-"*30)

    action = -1

    while (True):
        print("1) Add a task")
        print("2) Delete a task")
        print("3) Print tasks")
        print("4) Exit")

        action = int(input())

        if action == 1:
            add_task_interface()
        elif action == 2:
            delete_task_interface()
        elif action == 3:
            show_tasks()

        elif action == 4:
            break

        else:
            print("Invalid choice")