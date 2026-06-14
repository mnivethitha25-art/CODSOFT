task_box = []
while True:
    print("\n---DAILY PLANNER---")
    print("A = Add Task")
    print("V = View Task")
    print("R = Remove Task")
    print("C = Check Total Task")
    print("E = Exit")

    option = input("Enter options: ").upper()
    if option == "A":
        work = input("Enter Task Name: ")
        task_box.append(work)
        print("New Task Added Successfully!")
    elif option == "V":
        if task_box:
            print("\nTasks:")
            count = 1
            for work in task_box:
                print(str(count)+"."+work)
                count += 1
            else:
                print("Task List Is Empty...")
    elif option == "R":
        if task_box:
            for i, work in enumerate(task_box, 1):
                print(i, work)
            try:
                remove_id = int(input("Which task number to remove? "))
                if 1 <= remove_id <= len(task_box):
                    removed_task = task_box.pop(remove_id - 1)
                    print("Removed...", removed_task)
                else:
                    print("Uh-oh! Wrong number...")
            except ValueError:
                print("Please, Enter a Valid Number")
        else:
            print("No Tasks Available...")
    elif option == "C":
        print("Total Tasks =", len(task_box))
    elif option == "E":
        print("See You Later! My Task Hub Is Closing....")
        break
    else:
        print("Please,Choose a Valid Option...")

