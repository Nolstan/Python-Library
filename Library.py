import csv
import os
# from fileinput import filename
import datetime
def Creating_Account_USER():
    name=input("Create your Full Name: ")
    while True:
            Password=input("Create Your Password: ")
            hasletters=any(char.isalpha() for char in Password)
            hasDigit=any(char.isdigit() for char in Password)
            hasSymbol=any(not char.isalnum() for char in Password)
            file_name=f"{name}_File.csv"
            if os.path.exists(file_name):
                print(f"{file_name} already Exist")
                return
            if len(Password)<8:
                print("A password MUST contain more than 7 characters")
            if hasletters and hasDigit and hasSymbol:
                with open(file_name,"a+",newline="") as csvFile:
                    csvWriter=csv.writer(csvFile)
                    csvWriter.writerow([name,Password])
                print("Account Created Succsessfully")
                main()
                return
            else:
                print("Weak Password.Please include letters,Digits and Symbols")

def Creating_Account_Admin():
    secret_ID=input("Enter your Admin ID")
    if secret_ID=="someword":

            name=input("Create your Full Name: ")
            Password=input("Create Your Password: ")
            while True:
                hasletters=any(char.isalpha() for char in Password)
                hasDigit=any(char.isdigit() for char in Password)
                hasSymbol=any(not char.isalnum() for char in Password)
                file_name=f"{name}_File.csv"
                if os.path.exists(file_name):
                    print(f"{file_name} already Exist")
                    return
                if len(Password)<8:
                    print("A password MUST contain more than 7 characters")
                if hasletters and hasDigit and hasSymbol:
                    with open(file_name,"a+",newline="") as csvFile:
                        csvWriter=csv.writer(csvFile)
                        csvWriter.writerow([name,Password])
                    print("Account Created Succsessfully")
                    break
                else:
                    print("Weak Password.Please include letters,Digits and Symbols")
    else:
        print("You are not Qualified to register as Admin")

def Login_Info_User():
    while True:
        name=input("Enter Username\n:>")
        password=input("Enter your Password\n:>")
        file_name = f"{name}_File.csv"
        if not os.path.exists(file_name):
            getOpt=input("Account Not Exist.Press 1 to create Account\n"
                         "Press any Key to Exit\n:>").strip()
            if getOpt == '1':
                Creating_Account_USER()
            else:
                print("Goodbye! Thanks.")
                return
        flag=False
        with open(file_name,"r")as f:
            csvReader=csv.reader(f)
            #next(csv_reader, None)  # Skip header row if present
            for row in csvReader:
                # Ensure the row has at least two elements (name and password)
                if len(row) >= 2 and row[0] == name and row[1] == password:
                    print("Congrats! You are in.")
                    flag=True
                    user_options()
                    return
            if not flag:
                print("Wrong Password/name Buddy!")
                opt = input("Press y to try again\n"
                            "Press any Key to Exit\n:>").lower()
                if opt == 'y':
                    continue  # Retry the process
                else:
                    print("Goodbye! Thanks.")
                    break  # Exit the loop and function
def user_options():
    while True:
        print("Choose\n"
    
              "1.Borrow a Book\n"
              "2.Search for a Book\n"
              "3.View Available Books\n"
              "4.View Borrowed Books\n"
              "5.Change Password\n"
              "6.Exit")
        try:
            sel = int(input(">"))
            if sel == 1:
                name = input("Enter The Book name\n:>")
                borrow_book(name)
                return
            elif sel == 2:
                searchBook_student()
                return
            elif sel == 3:
                view_available_books_student()
                return
            elif sel == 4:
                view_borrowed_books_student()
                return
            elif sel == 5:
                pass
            else:
                print("Thank you for using the Library")
                return
        except ValueError:
            print("Enter an Interger")
        return

def Admin_options():
    while True:
        try:
     
            choice = int(input("Choose\n"
                               "1.Add a Book\n"
                               "2.Update Book Information\n"
                               "3.List All Books\n"
                               "4.Remove a User(Student)\n"
                               "5.Delete a Book\n"
                               "6.View all borrowed books\n"
                               "7.View all Available books\n"
                               "8.Record a return Book\n"
                               "9.Search for a Book\n"
                               "10.Total Books In the Library\n"
                               "11.Exit"
                               ":>"))

            if choice == 1:
                add_Book()
            elif choice == 2:
                update_Book_Info()
            elif choice == 3:
                list_ALL_BOOks()
            elif choice == 4:
                remove_User()
            elif choice == 5:
                remove_Book()
            elif choice == 6:
                view_borrowed_books_Admin()
            elif choice == 7:
                view_available_books_Admin()
            elif choice == 8:
                record_returned_book()
            elif choice == 9:
                searchBook_Admin()
            elif choice == 10:
                Total_Books()
            elif choice == 11:
                print("Exiting...")
                break
            return
        except ValueError:
            print("Enter an Interger")

def Login_Info_Admin():
    while True:
        secret=input("Enter your Id\n:>")
        if secret =="someword":
            name=input("Enter Username\n:>")
            password=input("Enter your Password\n:>")
            file_name = f"{name}_File.csv"
            if not os.path.exists(file_name):
                choose=input("File Does Not Exist ,Press y to try again\n"
                             "Press any Key to Exit\n:>").lower()
                if choose=="y":
                    continue  # Retry the process
                else:
                    print("Goodbye! Thanks.")
                    break  # Exit the loop and function
            with open(file_name,"r")as f:
                csvReader=csv.reader(f)
                #next(csv_reader, None)  # Skip header row if present
                for row in csvReader:
                    # Ensure the row has at least two elements (name and password)
                    if len(row) >= 2 and row[0] == name and row[1] == password:
                        print("Congrats! You are in.")
                        Admin_options()
                        break
                    else:
                        print("Wrong Password/name")
                        opt = input("Press y to try again\n"
                                    "Press any Key to Cancel The process\n:>").lower()
                        if opt == 'y':
                            continue  # Retry the process
                        else:
                            print("Goodbye! Thanks.")
                            break  # Exit the loop and function
        else:
            print("Sorry U do not have admin priviledge")
        return

def add_Book():
    file_name = "List_Of_BOOKS.csv"
    if not os.path.exists(file_name):
        open(file_name, 'w').close()
    try:
        total = int(input("Enter the Total Number of Books to be Recorded: "))
        if total <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Read existing books into memory for duplicate checks
    existing_books = []

    with open(file_name, "r", newline="") as f:
        csvreader = csv.reader(f)
        existing_books = [row for row in csvreader]

    # Loop to record multiple books
    for i in range(total):
        while True:
            print(f"\nRecording details for Book {i + 1}:")
            name = input("Enter Book Name: ").strip()
            ISBN = input("Enter ISBN Number: ").strip()
            status = input("Enter Book Status (e.g., Available, Borrowed): ").strip()

            # Validate input
            if not name or not ISBN or not status:
                print("All fields are required. Please try again.")
                continue

            # Check for duplicates
            duplicate_name = any(row[0].strip().lower() == name.lower() for row in existing_books)
            duplicate_ISBN = any(row[1].strip() == ISBN for row in existing_books)

            if duplicate_name:
                print(f"Book '{name}' already exists. Please try again.")
                continue
            if duplicate_ISBN:
                print(f"ISBN '{ISBN}' already exists. Please try again.")
                continue

            # Add the new book to the file
            with open(file_name, "a", newline="") as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow([name, ISBN, status])
                print(f"Book '{name}' has been added successfully.")

            existing_books.append([name, ISBN, status])
            break  # Exit the input loop for this book

    print("\nAll books have been recorded successfully.")
    Admin_options()

def list_ALL_BOOks():
    filename= "List_Of_BOOKS.csv"
    if not os.path.exists(filename):
        print("The file Does Not Exist.Sorry")
        return
    with open(filename,"r")as f:
        csvreader=csv.reader(f)
        print("ALL BOOKS IN THIS LIBRARY")
        print("*"*50)
        i=0
        for row in csvreader:
            i += 1
            print(f"({i}.{row}")
        print("*" * 50)
        Admin_options()

def Total_Books():
    filename= "List_Of_BOOKS.csv"
    if not os.path.exists(filename):
        print("The file Does Not Exist.Sorry")
        return
    with open(filename,"r")as f:
        csvreader=csv.reader(f)
        print("SUM OF ALL BOOKS")
        print("*"*50)
        i=0
        for row in csvreader:
            i += 1
        print(f"There Are a Total of {i} Books In this Library")
        print("*" * 50)
        Admin_options()

def update_Book_Info():
    filename = "List_Of_BOOKS.csv"

    if not os.path.exists(filename):
        print("The file does not exist. Sorry!")
        return
    while True:
        name = input("Enter the book name to update: ").strip()
        updated = False
        temp_file = "temp_books.csv"
        with open(filename, "r", newline="") as f, open(temp_file, "w", newline="") as temp:
            csvreader = csv.reader(f)
            csvwriter = csv.writer(temp)
            for row in csvreader:
                if row[0] == name:
                    print(f"Book '{name}' found.")
                    number = int(input(
                        "Select\n 1. To Change Name of the Book\n 2. To Change ISBN number of the book\nYour choice: "))
                    if number == 1:
                        new_name = input("Enter the new name: ").strip()

                        # Check for duplicate name
                        if new_name == name:
                            print("The new name is the same as the current name. No changes made.")
                            csvwriter.writerow(row)
                            updated = True
                            continue
                        # Write updated row
                        csvwriter.writerow([new_name, row[1]])
                        print(f"Book name updated to '{new_name}'.")
                        updated = True
                    elif number == 2:
                        new_isbn = input("Enter the new ISBN number: ").strip()
                        # Check for duplicate ISBN
                        if new_isbn == row[1]:
                            print("The new ISBN is the same as the current ISBN. No changes made.")
                            csvwriter.writerow(row)
                            updated = True
                            continue
                        # Write updated row
                        csvwriter.writerow([row[0], new_isbn])
                        print(f"ISBN number updated to '{new_isbn}'.")
                        updated = True
                    else:
                        print("Invalid choice. No changes made.")
                        csvwriter.writerow(row)
                        updated = True
                else:
                    # Write unchanged row
                    csvwriter.writerow(row)
        # If book not found
        if not updated:
            print("The book does not exist. Try again? (y/n)")
            try_again = input().lower()
            if try_again == "y":
                continue
            else:
                os.remove(temp_file)# Clean up temp file
                Admin_options()
                return
        # Replace the original file with the updated file
        os.replace(temp_file, filename)
        print("Book information updated successfully!")
        Admin_options()
        break

import shutil
def borrow_book(name):
    filename = "List_Of_BOOKS.csv"
    temp_file = "temp_books.csv"

    # Check if the file exists
    if not os.path.exists(filename):
        print("The file does not exist. Sorry!")
        return

    while True:
        try:
            # Open the original and temporary files
            with open(filename, "r", newline="") as f, open(temp_file, "w", newline="") as temp:
                csvreader = csv.reader(f)
                csvwriter = csv.writer(temp)
                book_found = False
                for row in csvreader:

                    if len(row) >= 3 and row[0].strip().lower() == name.strip().lower() and row[2].strip().lower() == "available":
                        print(f"Book '{name}' found and borrowed successfully!")
                        row[2] = "Borrowed"  # Update availability status
                        book_found = True

                    csvwriter.writerow(row)  # Write each row to the temp file
            if book_found:
                shutil.move(temp_file, filename)
                print("Library updated successfully!")
                return
            again = input(
                f"Sorry, the book '{name}' is either not available or not in our library.\n"
                f"Press 'y' to search for another book or any other key to exit: "
            )
            if again.strip().lower() != "y":
                print("Thank you for using this library. Goodbye!")
                return
            name = input("Enter the name of the book you want to borrow: ").strip()
        except PermissionError:
            print("Permission denied. Make sure the file is not open elsewhere and you have write access.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

def searchBook_Admin():
    while True:
        print("SEARCH FOR ANY AVAILABLE BOOK IN THE LIBRARY")
        name = input("Enter Name of the Book\n:> ")
        filename = "List_Of_BOOKS.csv"

        if not os.path.exists(filename):
            print("The file does not exist. Sorry!")
            return

        with open(filename, "r") as f:
            csvreader = csv.reader(f)
            book_found = False
            continue_searching = False
            for row in csvreader:
                if len(row) >= 2 and row[0].lower() == name.strip().lower():
                    print("*"*50)
                    print(f"{row}")
                    print("*"*50)
                    book_found = True
                    Admin_options()
                    return
            if not book_found:
                search=input("Book not found.To Search Again press y\n"
                      "Else any other key to exit")
                if search.lower() == "y":
                    continue
                Admin_options()
                return
def searchBook_student():
    while True:
        print("SEARCH FOR ANY AVAILABLE BOOK IN THE LIBRARY")
        name = input("Enter Name of the Book\n:> ")
        filename = "List_Of_BOOKS.csv"

        if not os.path.exists(filename):
            print("The file does not exist. Sorry!")
            return

        with open(filename, "r") as f:
            csvreader = csv.reader(f)
            book_found = False
            continue_searching = False
            for row in csvreader:
                if len(row) >= 2 and row[0].lower() == name.lower():
                    book_found = True
                    if row[2].lower() == "available":
                        sel=input(f"Book '{name}' found\n"
                              "Press y to borrow it\n"
                              "Press any Key to Cancel The process\n:>").lower()
                        if sel == "y":
                            borrow_book(name)
                        print("Thank you. Bye!")
                    else:
                        tryingagain=input(f"'{name}' is Found But currently borrowed.\n"
                                              f"Press y Search for Another Book\n"
                                              f"Press any Key to Cancel The process\n:>").lower()
                        if tryingagain == "y":
                            continue_searching = True
                            continue
                    if not continue_searching:
                        user_options()#print("Thank you. Bye!")
                        return

            if not book_found:
                again=input(f"Sorry, the book '{name}' does not exist in our library.\n"
                            f"Press y to Search for Another Book\n"
                            f"Press any Key to Cancel The process\n:>").lower()
                if again == "y":
                    continue
                print("THANK YOU")
                user_options()
                break

#".Record a return Book"
def record_returned_book():
    while True:

        filename = "List_Of_BOOKS.csv"
        if not os.path.exists(filename):
            print("The file does not exist. Sorry!")
            return
        name=input("Enter Name of the Book: >")
        book_found = False
        temp_file = "temp_books.csv"
        with open(filename, "r", newline="") as f, open(temp_file, "w", newline="") as temp:
            csvreader = csv.reader(f)
            csvwriter = csv.writer(temp)
            for row in csvreader:
                if len(row) >= 2 and row[0].lower() == name.lower() and row[2].lower() == "borrowed".lower():
                    book_name=input(f"Book '{name}' found press y to return it. "
                                    f"press any key to cancel the Process >").lower()
                    book_found = True
                    if book_name == "y":
                        update=input("Type (Available) to mark the book returned >").lower()
                        if update != 'available':
                            print("Please Make sure you have entered the correct Spelling for 'Available'")
                            return
                        else:
                            row[2] = update
                    else:
                        print("Thank you. Bye!")
                        return
                # Write all rows back to the file temp (updated or unchanged)
                csvwriter.writerow(row)
            if not book_found:
                tryagain=input(f"Sorry, the book '{name}' \n"
                               f"Might Already be Available else Does Not Exist\n"
                               f"Press 'y' to Search for another Book and Any key to cancel The process\n: >").lower()
                if tryagain == "y":
                    continue
                else:
                    print("Thank you. Bye!")
                    Admin_options()
                break

        shutil.move(temp_file, filename)  # Replace os.replace with shutil.move
        print(f"Book '{name}' is now Available.")
        Admin_options()
        break
def  view_borrowed_books_Admin():
    filename = "List_Of_BOOKS.csv"
    if not os.path.exists(filename):
        print("The file does not exist. Sorry!")

    with open(filename, "r", newline="") as F:
        csvreader = csv.reader(F)
        print("ALL BORROWED BOOKS")
        print("*"*50)
        while True:
            for row in csvreader:
                if len(row) >= 2 and row[2].lower() == 'borrowed':
                    print(f"'{row[0]}' was borrowed (Implement a date ).")
            print("*"*50)
            Admin_options()
            return
def  view_borrowed_books_student():
    filename = "List_Of_BOOKS.csv"
    if not os.path.exists(filename):
        print("The file does not exist. Sorry!")

    with open(filename, "r", newline="") as F:
        csvreader = csv.reader(F)
        print("ALL BORROWED BOOKS")
        print("*"*50)
        while True:
            for row in csvreader:
                if len(row) >= 2 and row[2].lower() == 'borrowed':
                    print(f"'{row[0]}' was borrowed (Implement a date ).")
            print("*"*50)
            user_options()
            return

def view_available_books_student():
    filename = "List_Of_BOOKS.csv"
    if not os.path.exists(filename):
        print("The file does not exist. Sorry!")
    with open(filename, "r", newline="") as F:
        csvreader = csv.reader(F)
        print("ALL AVAILABLE BOOKS")
        print("*" * 50)
        while True:
            for row in csvreader:
                if len(row) >= 2 and row[2].lower() == 'available':
                    print(f"'{row[0]}'")
            print("*" * 50)
            what=input("Do you want to Borrow any Book?\n"
                  "Press y to proceed and Any key to deny\n:>").lower()
            if what == "y":
                name=input("Choose AnyBook from the list\n:>")
                borrow_book(name)
                return
            else:
                print("Thank you")
                user_options()
                return
def view_available_books_Admin():
    filename = "List_Of_BOOKS.csv"
    if not os.path.exists(filename):
        print("The file does not exist. Sorry!")
    with open(filename, "r", newline="") as F:
        csvreader = csv.reader(F)
        print("ALL AVAILABLE BOOKS")
        print("*" * 50)
        while True:
            for row in csvreader:
                if len(row) >= 2 and row[2].lower() == 'available':
                    print(f"'{row[0]}'")
            print("*" * 50)
            what=input("Do you want to Borrow any Book?\n"
                  "Press y to proceed and Any key to deny\n:>").lower()
            if what == "y":
                name=input("Choose AnyBook for the list\n:>")
                borrow_book(name)
                return
            else:
                print("Thank you for using this Library. Bye!")
                Admin_options()
                return
def remove_Book():
    remaining_books=[]
    name=input("Name of the Book\n:>")
    file_name = "List_Of_BOOKS.csv"
    if not os.path.exists(file_name):
        print("File does not exits")
        Admin_options()
        return
    temp="temp_file.csv"
    book_found=False
    try:
        with open(file_name,newline='')as f,open(temp,"a",newline='') as f2:
            csvreader=csv.reader(f)
            csvwriter=csv.writer(f2)

            for row in csvreader:
                if len(row)>2 and row[0].lower()!=name.lower():
                    # remaining_books.append(row)
                    csvwriter.writerow(row)
                    book_found=True

    except Exception:
        print("Book Not found ")
        return
    if book_found:
        shutil.move(temp, file_name)
        print("Book removed succsessfulyy")
        Admin_options()
        return
    else:
        os.remove(temp)
        Admin_options()

def remove_User():
    name=input("Who Do you want to Terminate\n:>")
    file_name = f"{name.lower()}_File.csv"
    if not os.path.exists(file_name):
        print("File name does not Exists")
        Admin_options()
        return
    else:
        os.remove(file_name)
        print(f"{name} has Been Removed from the Library")
        Admin_options()
        return

def main():
      while True:
          try:
              print("*" * 50)
              print("\nWELCOME TO THE LIBRARY\n"
                    "Choose\n"
                    "1. Create Account as Student\n"
                    "2. Create Account as Admin\n"
                    "3. Login (Admin)\n"
                    "4. Login (student)\n"
                    "5. Exit")
              print("*" * 50)
              sel = int(input("Your choice> "))

              if sel == 1:
                  Creating_Account_USER()  # Function for creating a student account
                  break
              elif sel == 2:
                 Creating_Account_Admin()  # Function for creating an admin account
                 break
              elif sel == 3:
                  Login_Info_Admin()  # Function for login functionality
                  break
              elif sel == 4:
                  Login_Info_User()
                  break
              elif sel == 5:
                  print("Goodbye!")
                  break  # Exit the loop and end the program
              else:
                  print("Invalid choice. Please select a number between 1 and 5.")
          except ValueError:
              print("ERROR! Please enter an integer.")

if __name__=="__main__":
      main()

