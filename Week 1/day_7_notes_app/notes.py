## NOTES APPLICATION

# Requirements

# add note
# view notes
# append new notes
# save permanently in a file

path = "E:\\Vidya Career\\IT JOB\\Repati Kosam\\rk_Projects\\Notes App\\file.txt"

# add note

def add_note(path):
    with open(path, "a") as f:
        n = input("Enter your note: ")
        f.write("\n"+n)
        print("--------------------------------------------------")
        print(f"Your note {n} has been added successfully.")
        print("--------------------------------------------------")
        print()
        return n

# print(add_note(path))

# view notes

def view_notes(path):
    with open(path) as f:
        print()
        print("The notes in your app:")

        for i in f:
            print(i.strip())

# view_notes(path)

while True:

    print("---------- WELCOME TO NOTES APPLICATION ----------")

    print("1. Add notes\n2. View notes\n3. Exit")

    ch = int(input("Enter the operation you need to perform: "))

    if ch == 1:
        add_note(path)

    elif ch == 2:
        view_notes(path)

    elif ch == 3:
        exit()

    else:
        print("Wrong Choice")