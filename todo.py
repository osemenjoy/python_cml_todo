name = input("Enter name: ")
email = input("Enter email: ")
menu = ['Add', 'Edit', 'Delete']

choice = 0
while choice != "0":
        print("What do you want to do to tasks... (Press 0 to exit)")
        for i in menu:
            print("-",i)

        choice = input("Enter Choice: ").lower()

        if choice == "add":
            task_name = 0
            while task_name != "0":
                task_name = input("Task (Press 0 to exit): ")
                if task_name == "0":
                    break
                f = open(f"{name}.txt","a")
                f.write(task_name)
                f.write("\n")
                f.close()
            view = input("Would you like to view your task? (y/n): ").lower()
            if view == "y":
                print("Your tasks are..")
                f = open(f"{name}.txt")
                print(f.read())
                f.close()
                print("Thank you for using  the program!")
            else:
                pass

        elif choice == "edit":
            print("Your tasks are..")
            f = open(f"{name}.txt")
            print(f.read())
            f.close()

            # edit task
            task_name = 0
            while task_name != "0":
                task_name = input("Task (Press 0 to exit): ")
                if task_name == "0":
                    break
                f = open(f"{name}.txt","a")
                f.write(task_name)
                f.write("\n")
                f.close()

                #view task
            view = input("Would you like to view your tasks? (y/n): ").lower()
            if view == "y":
                print("Your tasks are..")
                f = open(f"{name}.txt")
                print(f.read())
                f.close()
                print("Thank you for using  the program!")
            else:
                pass

        elif choice == "delete":
            filename = f"{name}.txt"
            
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    print("Your tasks are:")
                    for line in lines:
                        print(line.strip())

                while True:
                    delete_task = input("Enter task to be deleted (Press Enter to exit): ").strip()
                    if not delete_task:
                        break

                    with open(filename, 'w') as file:
                        for line in lines:
                            if line.strip() != delete_task:
                                file.write(line)

                    print(f"Task '{delete_task}' deleted successfully.")

                    with open(filename, 'r') as file:
                        lines = file.readlines()

            except FileNotFoundError:
                print("File not found.")
            
            view = input("Would you like to view your tasks? (y/n): ").strip().lower()
            if view == "y":
                try:
                    with open(filename, 'r') as file:
                        print("Your updated tasks are:")
                        print(file.read())
                except FileNotFoundError:
                    print("File not found.")
            
            print("Thank you for using the program!")