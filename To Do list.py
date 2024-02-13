Tasks = []
def add():
  task = input("Please enter a task: ")
  Tasks.append(task)
  print(f"Task '{task}' added to the list.")

def list():
  if not Tasks:
    print("No Tasks Yet , Create One !")
  else:
    print("Tasks:")
    for index, task in enumerate(Tasks):
      print(f"Task Number {index}: {task}")

def delete():
  try:
    listTasks()
    if Tasks:
      Delete = int(input("Enter the Task Number to delete: "))
      if Delete >= 0 and Delete < len(Tasks):
        Tasks.pop(Delete)
        print(f"Task Number {Delete} has been removed.")
      else:
        print(f"Task Number {Delete} was not found.")
  except:
    print("No Tasks Yet , Create One !")


if __name__ == "__main__":
  
  print("Python To do list ")
  while True:
    print("")
    print("Please select one of the following options:")
    print("")
    print("Enter 1 to Add a new Task")
    print("Enter 2 to Delete a Task")
    print("Enter 3 to List All the Tasks")
    print("Enter 4 to Quit")

    x = input("Enter your choice: ")

    if (x == "1"):
      add()
    elif (x == "2"):
      delete()
    elif (x == "3"):
      list()
    elif (x == "4"):
      break
    else:
      print("Invalid input,Please try again !")

  print("")
