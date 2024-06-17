def add_book(library,title,author):
    library[title] = author
    print("Book added successfully!")

def view_book(library):
    if not library:
        print("No books avaliable!")
    else:
        print("BOOKS AVALIABLE :")
        print("Title\t\t|\tAuthor")
        for key in library:
            print("{}\t|\t{}".format(key,library.get(key)))

def delete_book(library,title):
    if title in library:
        del library[title]
        print("Deleted Successfully!")
    else:
        print("Book not present.")

def search_book(library,author):
    for title,author1 in library.items():
        if author == author1:
            print("Book found.")
            print(f"Searched book:{title}\nAuthor name:{author}")

def main():
    library = {}

    print("*************************")
    print("Library Management System")
    print("*************************")

    while True:
        print()
        print("1.Add Book\n2.View Books\n3.Delete Book\n4.Search Book\n5.Exit")
        choice = int(input("Enter your choice :"))

        match choice:
            case 1:
                title = input("Enter the book name :")
                author = input("Enter the author :")
                add_book(library,title,author)
            case 2:
                view_book(library)
            case 3:
                title = input("Enter the title of book to delete :")
                delete_book(library,title)
            case 4:
                author = input("Enter the author of book to search :")
                search_book(library,author)
            case 5:
                break 
            case _:
                print("Invalid input!!")

main()
                           