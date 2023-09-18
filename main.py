import Authentication
import Recommend
Authentication.authenticate()
if Authentication.authenticated==True:
    choice=input("What do you want to do (See the books you have read, Add a new book, Get a recommendation of what next to read)? ")
    if choice=="See the books you have read":
        with open(Authentication.userid, "r") as books:
            read=books.read()
            print(read)
            books.close()
    elif choice=="Add a new book":
        addbook=input("Which book do you want to add? ")
        with open(Authentication.userid, "a") as books:
            books.write(addbook)
            books.write("\n")
            books.close()
    elif choice=="Get a recommendation of what next to read":
        query = input("What is your favourite book? ")  # Replace with your book title or author query
        recommended_books = Recommend.search_books(query)
        print(recommended_books)
            
    