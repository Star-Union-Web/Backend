import json

data ={}

def MenuShow ():
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Save the changes")
    print("6. Exit")
    print("======================")
    print("Please choose an option from 1-6")

def date_validation1 (date):
    while date.count('-')!=1:
        date = input("please enter the task's due date in (day-month) format: ")
    return date

def date_validation2 (valid_days,valid_months,day,month):
    while day not in valid_days or month not in valid_months:
        date = input("Invalid Input,please enter the task's due date in (day-month) format: ")
        date = date_validation1(date)
        date_list = date.split('-')
        day = date_list[0]
        month = date_list[1]

    return day,month

def date_validation3 (month):
    if month =='2':
        available_days =  [ str(n) for n in range(1,30)]

    elif (int(month)<=7 and int(month)%2==1) or (int(month)>7 and int(month)%2==0):
         available_days =  [ str(n) for n in range(1,32)]

    elif (int(month)<7 and int(month)%2==0) or (int(month)>7 and int(month)%2==1):
         available_days =  [ str(n) for n in range(1,31)]

    return available_days

def full_date_validation(date):
    date = date_validation1(date)
   
    
    date_list = date.split('-')
    day = date_list[0]
    month = date_list[1]
   
    valid_days = [ str(n) for n in range(1,32)]
    valid_months = [ str(n) for n in range(1,13)]
    
    
    day,month=date_validation2(valid_days,valid_months,day,month)
   
    available_days = date_validation3(month)
    
    while day not in available_days:
        print ("this date cannot be found")
        date = input("enter the task's due date in (day-month) format: ")
        date = date_validation1(date)
        
        date_list = date.split('-')
        day = date_list[0]
        month = date_list[1]
        day,month = date_validation2(valid_days,valid_months,day,month)
        available_days = date_validation3(month)

    return day,month

def descrip_validation(desc):
    while len(desc)==0:
        print("the description is empty, please enter a description for your task: ")
        desc = input("Please Enter theTask description: ")
    return desc

def priority_validation(prio):
    priority_choices = ['LOW','MEDIUM','HIGH']
    while prio.upper() not in priority_choices:
        print ("the priority is invalid ,please enter a valid one")
        prio = input("Please enter the Priority of your task: ")
    return prio


def Add_task ():
    name = str((len(data)+1))
    desc = input("Please Enter theTask description: ")
    desc  = descrip_validation(desc)

    prio = input("Please enter the Priority of your task(high ,medium , low): ")
    
    prio = priority_validation(prio)

    date = input("enter the task's due date in (day-month) format: ")
    
    day,month = full_date_validation(date)

        
    date = day+'-'+month

    data[name]= {"description": desc , "priority" : prio , "date" : date}
   

def show_tasks():
    
    
    print('=============================================')

    
    for indx,value in zip(data.keys(),data.values()):
        print (f" Task {indx}: the description: {value.get('description')}, the priority of it is {value.get('priority')} ,the DUE DATE is on {value.get('date')}")
        
    print('=============================================')

def deleteTask():
    if(len(data)==0):
        show_tasks()
        print('the task list is already empty')
        print ('')
        return
    show_tasks()
    choices_list = [str(a) for a in range (1,len(data)+1)]
    choice = input("enter the number of the task that you want to delete: ")
    

    while choice not in choices_list:
        print('invalid task to delete , please enter a valid one')
        show_tasks()
        choice = input("enter the number of the task that you want to delete")


    name =  choice
    print(f"deleting { name }")
    data.pop(name)
    
    
    new_dic = {str(idx): value for idx, value in enumerate(data.values(), start=1)}

    
    data.clear()
    i=1
    for value in new_dic.values():
        data[str(i)] = {"description": value['description'] , "priority" : value['priority'] , "date" : value['date']}
        i+=1
           
def Update_Task ():
    show_tasks()

    if len(data) == 0:
        print("the task list is empty")
        print('')
        return
    
    choices_list = [str(a) for a in range (1,len(data)+1)]
    choice = input("enter the number of the task that you want to update: ")

    while choice not in choices_list:
        print('invalid task to update , please enter a valid one: ')
        show_tasks()
        choice = input("enter the number of the task that you want to update: ")

    name =  choice
    print(f"updating { name }")
    desc = input("Please Enter theTask description: ")
    desc = descrip_validation(desc)

    prio = input("Please enter the Priority of your task(high , medium ,low): ")
    prio = priority_validation(prio)

    date = input("enter the task's due date in (day-month)format: ")
    day,month = full_date_validation(date)

    date = day+'-'+month

    data.update( {name : {'description' : desc , 'priority' : prio , 'date' : date }} )
    
def save_changes ():
    with open('description.json' , 'w') as file:
            json.dump(data,file)   
    print("the data is saved successfully")
    print('')



with open('description.json', 'r') as file:
    try:
        data = json.load(file)  
    except :
        data = {}  

while (True):

    MenuShow()
    choice = input("Enter your choice: ")
    choices = ['1','2','3','4','5','6']

    while choice not in choices:
       print("Invalid choice ,Please Enter a valid one:")
       MenuShow()
       choice = input("Enter your choice: ")

    if(choice=='6'):
        with open('description.json' , 'w') as file:
            json.dump(data,file)   

        print("all the data has been saved automatically")
        print("exitting the program\n ======== \n BYE BYE")
        break
    
    
    
    if choice =='2':
        Add_task()

    elif choice=='1':
        show_tasks()

    elif choice=='3':
        Update_Task()

    elif choice=='4':
        deleteTask()

    elif choice =='5':
        save_changes()
