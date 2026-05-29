import json
tasks=[]#storage..we are using lists so it allows duplicates also
# LOAD TASK FROM FILE

try:
    with open("tasks.json","r") as file:
        tasks=json.load(file)#directly converts json file into python data
except FileNotFoundError:
    tasks=[]#file does not exist so creates an empty task list and allows app to  continue running
def save_tasks():
    with open("tasks.json","w") as file:
         json.dump(tasks,file)

print("welcome to TO-DO APP")#welcome message

#MAIN LOOP
while True:#main loop it will be running until user exits the app
    #show menu
    print("\n1.add task")
    print("2.show task")
    print("3.Delete task")
    print("4.completed tasks")
    print("5.update task")
    print("6.Exit")

    #Decision making
    choice=input("enter choice:")#we are using strings if user enters hello means it will be invalid choice,,if we use integer as input means if users enters hello it shows value error..

    #ADD TASK
    if choice == "1":#feature 1
        task = input("enter the task:")
        tasks.append({    # you can store mutliple pieces of information for each code,but it lists only task name can be stored
            "title":task,
            "completed":False
        })# if you want to add function separately you can do in between here
        save_tasks()
        print("task added successfully")


    #VIEW TASKS
        """elif choice== "2":#you can use this also as choice 2
        counter =1
        for x in tasks:
            print(counter,x)
            counter+=1"""
    elif choice == "2":#feature2
        if len(tasks)==0:
            print("No tasks available")
        else:
            for x,y in enumerate(tasks,1):#here x is index and y is total dictionary
                status = "☑️" if y["completed"] else "❌"#you can put done and not done instead of right and wrong symbol
                print(x,"-",y["title"],"-",status)


    #DELETE TASK
    elif choice == "3":
        delete_task=int(input("enter the task number:"))#we need to give interger input only because strings cannot be subtracted
        if 1 <=delete_task<=len(tasks):
            tasks.pop(delete_task-1)#-1 is given because you had started indexing from number 1 instead of 0
            save_tasks()
            print("deleted task number:",delete_task)
        else:
            print("invalid task")

    #COMPLETED TASK
    elif choice == "4":
        completed_task_number=int(input("enter task number:"))
        if 1<=completed_task_number<=len(tasks):
            tasks[completed_task_number-1]["completed"]=True
            save_tasks()
            print("completed task:",completed_task_number)
        else:
            print("invalid task")

    # UPDATED TASK
    elif choice == "5":
        update_task_number=int(input("enter task number:"))
        if 1<=update_task_number<=len(tasks):
            new_title=input("enter new task:")
            tasks[update_task_number-1]["title"]=new_title
            save_tasks()
            print("updated task;",update_task_number)
        else:
            print("invalid task")

    # TO EXIT APP
    elif choice == "6":#feature3
        break

    # IF YOU ENTER WRONG CHOICE
    else:#invalid file handling
        print("invalid choice")