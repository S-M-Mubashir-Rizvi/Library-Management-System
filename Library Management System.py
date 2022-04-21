class LibraryManagementSystem:
    def __str__(self):
        sorted_books = self.sort_books()
        print("-" * 100)
        for book in range(len(sorted_books)):
            strg1 = "NO.       TITLE"
            strg2 = "QUANTITY  FLOOR     AUTHOR NAME"
            strg1 += f"\n{str(book+1):10}{sorted_books[book][0]}"
            strg2 += f"\n{sorted_books[book][2]:10}{sorted_books[book][3]:10}{sorted_books[book][1]}"
            strg = strg1+"\n\n"+strg2
            print(strg)
            print("-"*100)
        return ""

    def login(self):
        print("Please fill the following credentials to login: ")
        email = input("Your email: ")
        passw = input("Your password: ")

        with open("Users.txt", "r+") as f:
            f.seek(0)
            content = f.readlines()
            users_list = []
            for user in content:
                user = user.split("-")
                last_item = user.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                user.append(LAST_ITEM)
                users_list.append(user)
            f.close()

        if [email, passw] in users_list:
            return [True, email, passw]
        else:
            return [False, email, passw]


    def signup(self):
        print("Welcome to the sign up page, please fill the following information: ")
        email = input("Enter your email: ")
        passw = input("Enter your password: ")

        with open("Users.txt", "r+") as f:
            f.seek(0)
            content = f.readlines()
            users_list = []
            for user in content:
                user = user.split("-")
                last_item = user.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                user.append(LAST_ITEM)
                users_list.append(user)
            f.close()

        for user in users_list:
            if email == user[0]:
                return False
            else:
                with open("Users.txt", "a+") as f:
                    to_add = email+"-"+passw
                    f.write("\n")
                    f.write(to_add)
                return True

    def cancelMembership(self):
        print("Please fill the following to cancel your membership: ")
        email = input("Enter your email: ")
        passw = input("Enter your password: ")

        with open("Users.txt", "r+") as f:
            f.seek(0)
            content = f.readlines()
            users_list = []
            for user in content:
                user = user.split("-")
                last_item = user.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                user.append(LAST_ITEM)
                users_list.append(user)
        to_remove = [email, passw]

        if to_remove in users_list:
            users_list.remove(to_remove)

        with open("Users.txt", "w+") as f:
            for user in users_list:
                if user != users_list[-1]:
                    to_write = user[0] + "-" + user[1]
                    f.write(to_write + "\n")
                else:
                    to_write = user[0] + "-" + user[1]
                    f.write(to_write)
            return True

    def add_book(self):
        with open("List_of_Books.txt", "a+") as f:
            f.seek(0)
            content = f.readlines()
            book_lists = []
            for book in content:
                book = book.split("-")
                last_item = book.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                book.append(LAST_ITEM)
                book_lists.append(book)
            f.close()

        print(self)
        print()

        book_name = input("Enter the book name you want to add: ")
        author_name = input("Enter the author name of the book: ")
        quantity = int(input("Enter the quantity you want to add: "))
        floor = int(input("Enter the floor number in which the book would be: "))

        with open("List_of_Books.txt", "a") as f:
            to_add = book_name+"-"+author_name+"-"+str(quantity)+"-"+"Floor"+str(floor)
            f.write("\n")
            f.write(to_add)

        return True


    def remove_book(self):
        with open("List_of_Books.txt", "a+") as f:
            f.seek(0)
            content = f.readlines()
            book_lists = []
            for book in content:
                book = book.split("-")
                last_item = book.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                book.append(LAST_ITEM)
                book_lists.append(book)
            f.close()

        print(self)
        print()

        book_name = input("Enter the book name you want to remove: ")
        quantity = int(input("Enter the quantity you want to remove: "))
        to_remove = ""

        for book in book_lists:
            if book[0] == book_name:
                to_remove = book
                break

        book_lists.remove(to_remove)

        if int(to_remove[2]) - quantity == 0:
            pass
        else:
            new_quantity = int(to_remove[2]) - quantity
            book_to_write = [to_remove[0], to_remove[1], str(new_quantity), to_remove[3]]
            book_lists.append(book_to_write)

        with open("List_of_Books.txt", "w+") as f:
            for book in book_lists:
                if book != book_lists[-1]:
                    to_write = book[0]+"-"+book[1]+"-"+book[2]+"-"+book[3]
                    f.write(to_write+"\n")
                else:
                    to_write = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                    f.write(to_write)
        return True


    def edit_book(self):
        with open("List_of_Books.txt", "a+") as f:
            f.seek(0)
            content = f.readlines()
            book_lists = []
            for book in content:
                book = book.split("-")
                last_item = book.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                book.append(LAST_ITEM)
                book_lists.append(book)
            f.close()

        print(self)
        print()

        book_name = input("Enter book name you want to edit: ")
        edit_book = None
        for book in book_lists:
            if book[0] == book_name:
                edit_book = book
        book_lists.remove(edit_book)


        while True:
            print("""Select a field you want to edit:
                     1.) Book Name
                     2.) Book Author
                     3.) Book Quantity
                     4.) Floor on which the book is located
                     5.) Exit""")

            choice = int(input("Enter your choice number: "))
            if choice == 1:
                book_name = input("Enter new name for the book: ")
                edit_book[0] = book_name
            if choice == 2:
                author_name = input("Enter new author name for the book: ")
                edit_book[1] = author_name
            if choice == 3:
                quantity = input("Enter new quantity for the book: ")
                edit_book[2] = quantity
            if choice == 4:
                book_floor = input("Enter new floor for the book: ")
                edit_book[3] = "Floor"+book_floor
            if choice == 5:
                break

        book_lists.append(edit_book)

        with open("List_of_Books.txt", "w+") as f:
            for book in book_lists:
                if book != book_lists[-1]:
                    to_write = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                    f.write(to_write + "\n")
                else:
                    to_write = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                    f.write(to_write)
        return True

    def search_book(self):
        book_name = ""
        author_name = ""
        while True:
            print("""Select a field you want to search:
                     1.) Book Name
                     2.) Book Author
                     3.) Exit""")
            choice = int(input("Enter your choice number: "))
            if choice == 1:
                book_name = input("Enter book name you want to search: ")
            if choice == 2:
                author_name = input("Enter author name you want to search: ")
            if choice == 3:
                break

        with open("List_of_Books.txt", "a+") as f:
            f.seek(0)
            content = f.readlines()
            book_lists = []
            for book in content:
                book = book.split("-")
                last_item = book.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                book.append(LAST_ITEM)
                book_lists.append(book)

            results_found = []
            for book in book_lists:
                if book[0] == book_name:
                    results_found.append(book)
                if book[1] == author_name:
                    results_found.append(book)

            return results_found

    def sort_books(self):
        with open("List_of_Books.txt", "a+") as f:
            f.seek(0)
            content = f.readlines()
            book_lists = []
            for book in content:
                book = book.split("-")
                last_item = book.pop()
                LAST_ITEM = ""
                for char in last_item:
                    if char == "\n":
                        continue
                    else:
                        LAST_ITEM = LAST_ITEM + char
                book.append(LAST_ITEM)
                book_lists.append(book)

        _len = len(book_lists)
        for i in range(_len-1):
            for j in range(_len-i-1):
                if book_lists[j] > book_lists[j+1]:
                    book_lists[j], book_lists[j+1] = book_lists[j+1], book_lists[j]
        return book_lists


    def renew_book(self):
        print("Welcome to the renew page, please login to continue.")
        success = self.login()

        if success[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            with open("Books_Informations.txt", "a+") as f:
                f.seek(0)
                content = f.readlines()
                bk_info = []
                for info in content:
                    info = info.split("-")
                    last_item = info.pop()
                    LAST_ITEM = ""
                    for char in last_item:
                        if char == "\n":
                            continue
                        else:
                            LAST_ITEM = LAST_ITEM + char
                    info.append(LAST_ITEM)
                    bk_info.append(info)
                f.close()
            book_name = input("Enter the book name you want to renew: ")

            for info in bk_info:
                if (success[1] == info[0]) and (info[1] == "check_out") and (info[2] == book_name):
                    bk_info.remove(info)

                    with open("Books_Informations.txt", "w+") as f:
                        f.write(success[1]+"-"+"renew"+"-"+book_name)
                        f.write("\n")

                        for info in bk_info:
                            if info != bk_info[-1]:
                                to_write = info[0]+"-"+info[1]+"-"+info[2]
                                f.write(to_write + "\n")
                            else:
                                to_write = info[0]+"-"+info[1]+"-"+info[2]
                                f.write(to_write)
            return True

    def check_out_book(self):
        print("Welcome to the check_out (borrow) page, please login to continue.")
        success = self.login()

        if success[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            with open("List_of_Books.txt", "a+") as f:
                f.seek(0)
                content = f.readlines()
                book_lists = []
                for book in content:
                    book = book.split("-")
                    last_item = book.pop()
                    LAST_ITEM = ""
                    for char in last_item:
                        if char == "\n":
                            continue
                        else:
                            LAST_ITEM = LAST_ITEM + char
                    book.append(LAST_ITEM)
                    book_lists.append(book)
                f.close()

            print(self)
            print()

            book_name = input("Enter book name you want to borrow: ")
            borrow_bk = None
            for book in book_lists:
                if book[0] == book_name:
                    borrow_bk = book
            book_lists.remove(borrow_bk)

            new_quantity = int(borrow_bk[2]) - 1
            updated_book = [borrow_bk[0], borrow_bk[1], str(new_quantity), borrow_bk[3]]
            book_lists.append(updated_book)

            with open("List_of_Books.txt", "w+") as f:
                for book in book_lists:
                    if book != book_lists[-1]:
                        to_write = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                        f.write(to_write + "\n")
                    else:
                        to_write = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                        f.write(to_write)

            with open("Books_Informations.txt", "a+") as f:
                f.write("\n")
                f.write(success[1]+"-check_out"+"-"+updated_book[0])
            return True


    def return_book(self):
        print("Welcome to the reserve page, please login to continue.")
        success = self.login()

        if success[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            with open("Books_Informations.txt", "a+") as f:
                f.seek(0)
                content = f.readlines()
                bk_info = []
                for info in content:
                    info = info.split("-")
                    last_item = info.pop()
                    LAST_ITEM = ""
                    for char in last_item:
                        if char == "\n":
                            continue
                        else:
                            LAST_ITEM = LAST_ITEM + char
                    info.append(LAST_ITEM)
                    bk_info.append(info)
                f.close()

            book_name = input("Enter the book name you want to return: ")
            for info in bk_info:
                if (success[1] == info[0]) and ((info[1] == "check_out") or (info[1] == "renew")) and (info[2] == book_name):
                    bk_info.remove(info)

                    with open("List_of_Books.txt", "a+") as f:
                        f.seek(0)
                        content = f.readlines()
                        book_lists = []
                        for info in content:
                            info = info.split("-")
                            last_item = info.pop()
                            LAST_ITEM = ""
                            for char in last_item:
                                if char == "\n":
                                    continue
                                else:
                                    LAST_ITEM = LAST_ITEM + char
                            info.append(LAST_ITEM)
                            book_lists.append(info)
                        f.close()

                    return_bk = None
                    for info in book_lists:
                        if info[0] == book_name:
                            return_bk = info

                    new_quantity = int(return_bk[2]) + 1
                    updated_book = [return_bk[0], return_bk[1], str(new_quantity), return_bk[3]]
                    book_lists.append(updated_book)

                    with open("List_of_Books.txt", "w+") as f:
                        for info in book_lists:
                            if info != book_lists[-1]:
                                to_write = info[0] + "-" + info[1] + "-" + info[2] + "-" + info[3]
                                f.write(to_write + "\n")
                            else:
                                to_write = info[0] + "-" + info[1] + "-" + info[2] + "-" + info[3]
                                f.write(to_write)

                    with open("Books_Informations.txt", "w+") as f:
                        for info in bk_info:
                            if info != bk_info[-1]:
                                to_write = info[0]+"-"+info[1]+"-"+info[2]
                                f.write(to_write + "\n")
                            else:
                                to_write = info[0]+"-"+info[1]+"-"+info[2]
                                f.write(to_write)
                        return True


    def reserve_book(self):
        print("Welcome to the reserve page, please login to continue.")
        success = self.login()

        if success[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            book_name = input("Enter the book name you want to reserve: ")
            with open("Books_Informations.txt", "a+") as f:
                f.write("\n")
                f.write(success[1]+"-reserve"+"-"+book_name)
            return True


obj = LibraryManagementSystem()

while True:
    print("""WELCOME TO OUR LIBRARY
                YOUR CAN PERFORM THE FOLLOWING FUNCTIONS:
                1.) Add a Book
                2.) Remove a Book
                3.) Edit a Book
                4.) Search a Book
                5.) View all Books
                6.) Check-Out or Borrow a Book
                7.) Renew a Book
                8.) Reserve a Book
                9.) Return a Book
                10.) Login
                11.) Signup
                12.) Cancel Membership
                13.) Exit""")
    choice = int(input("Please enter your desired option number: "))

    if choice == 1:
        boolean = obj.add_book()
        if boolean:
            print("Record added successfully")
        else:
            print("Something went wrong, operation unsuccessful")
        print("-" * 100)

    if choice == 2:
        boolean = obj.remove_book()
        if boolean:
            print("Record removed successfully")
        else:
            print("Something went wrong, operation unsuccessful")
        print("-" * 100)

    if choice == 3:
        boolean = obj.edit_book()
        if boolean:
            print("Record edited successfully")
        else:
            print("Something went wrong, operation unsuccessful")
        print("-" * 100)

    if choice == 4:
        search_results = obj.search_book()
        for item in search_results:
            print(item)
        print("_"*100)

    if choice == 5:
        print(obj)

    if choice == 6:
        boolean = obj.check_out_book()
        if boolean:
            print("Check Out Successful")
        else:
            print("Something went wrong, operation unsuccessful")
        print("-"*100)

    if choice == 7:
        boolean = obj.renew_book()
        if boolean:
            print("Your book has been renewed")
        else:
            print("Sorry, operation unsuccessful")
        print("-"*100)

    if choice == 8:
        boolean = obj.reserve_book()
        if boolean:
            print("Reservation Successful")
        else:
            print("The reservation for you book was unsuccessful")
        print("-"*100)

    if choice == 9:
        boolean = obj.return_book()
        if boolean:
            print("Thank you for returning the book, have a great day!")
        else:
            print("Something went wrong, operation unsuccessful")
        print("-"*100)

    if choice == 10:
        boolean = obj.login()
        if boolean[0]:
            print("Login Successful")
        else:
            print("Sorry, login was unsuccessful")
        print("-"*100)

    if choice == 11:
        boolean = obj.signup()
        if boolean:
            print("Signup Successful")
        else:
            print("Sorry, the email you entered is already registered with an account.")
        print("-"*100)

    if choice == 12:
        boolean = obj.cancelMembership()
        if boolean:
            print("Your membership is now cancelled. Have a great day!")
        else:
            print("Something went wrong, unsuccessful cancellation.")
        print("-"*100)

    if choice == 13:
        break
