daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isNum(char):
    if char >= '0' and char <= '9':
        return True
    else:
        return False
    

def handle_date(date):
    isCorrect = False
    while isCorrect == False:
        year = 0
        month = 0
        day = 0
        slashes = 0
        commas = 0
        columns = 0
        hours = 0
        minutes = 0
        str=""
        
        
        for i in range(len(date)):
            if isNum(date[i]):
                str+=date[i]

            if date[i] == '/':
                slashes+=1

            if date[i] == ',':
                commas+=1

            if date[i] == ':':
                columns+=1


            if (slashes == 1 and date[i] == '/'):
                year=int(str)
                str=""

            elif slashes == 2 and date[i] == '/':
                month=int(str)
                str=""


            if commas == 1 and date[i] == ',':
                day = int(str)
                str=""

            if columns == 1 and date[i] == ':':
                hours = int(str)
                str=""
            
            
                
        minutes = int(str)
        str=""

        if (slashes != 2 or commas != 1 or columns != 1):
            date = input("Invalid Date Format. Please Use the format (YYY/MMM/DDD, HH:MM): ")
        elif(minutes<0 or minutes > 59 or hours < 0 or hours > 23 ):
            date = input("Wrong Time. Try Again!: ")
        elif (month < 1 or month > 12 or day < 1 or day > daysInMonth[month-1]):
            date = input("Wrong Date. Try Again!: ")
        else:
            isCorrect = True


    return f"{year}/{month}/{day}, {hours}:{minutes}"
        
   

def handle_priority(priority):
    if (priority > 3):
        return 3
    elif (priority < 1):
        return 1
    else:
        return priority

inp = ""

def handleIdx(idx, sz):
    isCorrect = False
    while isCorrect == False:
        if (idx>=1 and idx<=sz):
            isCorrect = True
            return idx
        elif idx<1:
            inp = input("Invalid ID. Did you mean 1?(Y/N): ")
            if "y" in inp or "Y" in inp:
                idx = 1
            else:
                idx = int(input("Enter Correct ID: "))
        elif idx>sz:
            inp = input(f"Invalid ID. Did you mean {sz}?(Y/N): ")
            if "y" in inp or "Y" in inp:
                idx = sz
            else:
                idx = int(input("Enter Correct ID: "))

    return idx
