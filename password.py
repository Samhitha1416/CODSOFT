import random
import string

def generate_password(length):
    #password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        #invalid input of length
        print("Invalid input. Please enter a valid number.")
        return

    if length <= 0:
        #if it's -ve num or 0
        print("Invalid length. Please enter a positive number.")
        return

    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
