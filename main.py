from library import Library

def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System!\nMain Menu\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            print("\nBook Operations\n1. Add new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
            book_choice = input("Select an option: ")

            if book_choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                publication_date = input("Enter publication date: ")
                library.add_book(title, author, isbn, publication_date)
                print("Book added successfully.")

            elif book_choice == '2':
                library_id = input("Enter your library ID: ")
                book_title = input("Enter the title of the book you would like to borrow: ")
                library.borrow_book(library_id, book_title)

            elif book_choice == '3':
                library_id = input("Enter your library ID: ")
                book_title = input("Enter the title of the book to return: ")
                library.return_book(library_id, book_title)

            elif book_choice == '4':
                identifer = input("Enter book ISBN or title to search: ")
                book = library.search_book(identifer)
                if book:
                    print(book)
                else:
                    print("Book not found.")

            elif book_choice == '5':
                library.display_books()

        elif choice == '2':
            print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
            user_choice =input("Select an option: ")

            if user_choice == '1':
                name = input("Enter user name: ")
                library_id = input("Enter library ID: ")
                library.add_user(name, library_id)
                print("User added successfully.")

            elif user_choice == '2':
                library_id = input("Enter library ID: ")
                user = next((u for u in library.users if u.get_library_id() == library_id), None)
                if user:
                    print(user)
                else:
                    print("User not found.")

            elif user_choice == '3':
                library.display_users()

        elif choice == '3':
            print("\nAuthor Operations:\n1. Add new author\n2. View author details\n3. Display all authors")
            author_choice = input("Select an option: ")

            if author_choice == '1':
                name = input("Enter author name: ")
                biography = input("Enter author biography: ")
                library.add_author(name, biography)
                print("Author successfully added!")

            elif author_choice == '2':
                name = input("Enter author name: ")
                author = next((a for a in library.authors if a.get_name() == name), None)
                if author:
                    print(author)
                else:
                    print("Author not found.")

            elif choice == '3':
                library.display_authors()

        elif choice == '4':
            print("\nGenre Operations\n1. Add new genre\n2. View genre details\n3. Display all genres")
            genre_choice = input("Select an option: ")

            if genre_choice == '1':
                name = input("Enter genre name: ")
                description = input("Enter genre description: ")
                library.add_genre(name, description)
                print("Genre added successfully.")

            elif genre_choice == '2':
                name = input("Enter genre name: ")    
                genre = next((g for g in library.genres if g.get_name() == name), None)
                if genre:
                    print(genre)
                else:
                    print("Genre not found.")

            elif genre_choice =='3':
                library.display_genres()

        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
    