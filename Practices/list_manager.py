#VY 2nd Shopping List Manager

shop_list = []

while True:
    action = input("What would you like to do with your list?(view, add, remove, exit): ")
    #Write your code here
    if action.strip().lower() == "view":
        if shop_list:
            print(f"Here is your current list: {shop_list}")
        else:
            print("List not found.")
    elif action.strip().lower() == "add":
        task = input("Enter your new task here: ")
        shop_list.append(task)
        print(f'"{task}" has been successfully added to your list.')
    elif action.strip().lower() == "remove":
        task = input("Enter the task you would like to remove: ")
        if task in shop_list:
            shop_list.remove(task)
            print(f'"{task}" has been successfully removed from your list.')
        else:
            print("Task is not found in list.")
    elif action.strip().lower() == "exit":
        print("Goodbye.")
        break
    else:
        print("That is not a valid option.")