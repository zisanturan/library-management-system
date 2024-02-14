class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0) 
        lines = self.file.readlines()
        for line in lines:
            book_info = line.strip().split(",")
            print("Book:", book_info[0], "| Author:", book_info[1])

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        lines = self.file.readlines()
        updated_books = []
        for line in lines:
            book_info = line.strip().split(",")
            if book_info[0] != title:
                updated_books.append(line)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print(f"Book with title '{title}' removed successfully.")

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

