# open write append file

print("\n== File Menu ==")
print("1. Read File")
print("2. Overwrite File")
print("3. Write File (append mode)")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n> Read File")
        try:
            with open("MyThoughts.txt") as file:
                print(file.read())
        except FileNotFoundError:
            print("[ File is not found ]")
    elif choice == '2':
        print("\n> Overwrite File")
        text = input("input text: ")
        try:
            with open("MyThoughts.txt", 'w') as file:
                file.write(text)
                print("[ File has been overwritten ]")
        except FileNotFoundError:
            print("[ File is not found ]")
    elif choice == '3':
        print("\n> Write File")
        text = input("input text: ")
        try:
            with open("MyThoughts.txt", 'a') as file:
                file.write(text)
                print("[ Text has been appended ]")
        except FileNotFoundError:
            print("[ File is not found ]")
    else:
        print("\n[ Invalid choice ]")

    print("\n== File Menu ==")
    print("1. Read File")
    print("2. Overwrite File")
    print("3. Write File (append mode)")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")