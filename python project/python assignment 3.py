from datetime import datetime, timedelta


catalog = {
    "001": {"title": "Book 1", "author": "Author 1", "quantity": 5},
    "002": {"title": "Book 2", "author": "Author 2", "quantity": 3},
    "003": {"title": "Book 3", "author": "Author 3", "quantity": 2}
}


users = {}


def display_catalog():
    print("Current Catalog:")
    print("ID\tTitle\t\tAuthor\t\tAvailable")
    for book_id, book_info in catalog.items():
        print(f"{book_id}\t{book_info['title']}\t{book_info['author']}\t{book_info['quantity']}")


def register_user(name):
    user_id = len(users) + 1
    users[user_id] = {"name": name, "checked_out": {}}
    print(f"User {name} registered with ID {user_id}")


def checkout_book(user_id, book_id):
    if user_id not in users:
        print("Invalid user ID.")
        return
    if book_id not in catalog:
        print("Invalid book ID.")
        return
    if catalog[book_id]["quantity"] == 0:
        print("Book not available for checkout.")
        return
    if len(users[user_id]["checked_out"]) >= 3:
        print("User has reached maximum checkout limit.")
        return
    users[user_id]["checked_out"][book_id] = datetime.now()
    catalog[book_id]["quantity"] -= 1
    print(f"Book '{catalog[book_id]['title']}' checked out successfully.")


def return_book(user_id, book_id):
    if user_id not in users:
        print("Invalid user ID.")
        return
    if book_id not in users[user_id]["checked_out"]:
        print("Book was not checked out by this user.")
        return
    return_date = datetime.now()
    checkout_date = users[user_id]["checked_out"][book_id]
    days_overdue = (return_date - checkout_date).days - 14
    if days_overdue > 0:
        fine = days_overdue * 1
        print(f"Book returned {days_overdue} days overdue. Fine: ${fine}")
    else:
        fine = 0
    catalog[book_id]["quantity"] += 1
    del users[user_id]["checked_out"][book_id]


def list_overdue_books(user_id):
    if user_id not in users:
        print("Invalid user ID.")
        return
    overdue_books = []
    total_fine = 0
    for book_id, checkout_date in users[user_id]["checked_out"].items():
        days_overdue = (datetime.now() - checkout_date).days - 14
        if days_overdue > 0:
            fine = days_overdue * 1
            overdue_books.append((book_id, fine))
            total_fine += fine
    if overdue_books:
        print("Overdue Books:")
        print("ID\tFine")
        for book_id, fine in overdue_books:
            print(f"{book_id}\t${fine}")
        print(f"Total Fine: ${total_fine}")
    else:
        print("No overdue books.")


def main():
    while True:
        print("\nLibrary Management System")
        print("1. Display Catalog")
        print("2. Register User")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. List Overdue Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_catalog()
        elif choice == "2":
            name = input("Enter user's name: ")
            register_user(name)
        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            book_id = input("Enter book ID to checkout: ")
            checkout_book(user_id, book_id)
        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            book_id = input("Enter book ID to return: ")
            return_book(user_id, book_id)
        elif choice == "5":
            user_id = int(input("Enter user ID: "))
            list_overdue_books(user_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
