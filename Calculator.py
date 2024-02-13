def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y


print("Please select one of the following options:")
print("Enter 1 for Add")
print("Enter 2 for Subtract")
print("Enter 3 for Multiply")
print("Enter 4 for Divide")

while True:
    choice = input("Enter the Operation Number: ")

    if choice in ('1', '2', '3', '4'):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '1':
            print(f"{x} + {y} = {add(x, y)}")

        elif choice == '2':
            print(f"{x} - {y} = {sub(x, y)}")

        elif choice == '3':
            print(f"{x} * {y} = {mul(x, y)}")

        elif choice == '4':
            print(f"{x} / {y} = {div(x, y)}")
        
        next = input("Let's do next calculation? (yes/no): ")
        if next == "no":
          break
    else:
        print("Invalid Input")
