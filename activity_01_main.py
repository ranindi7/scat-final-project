""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""
import os

from library_item.library_item import LibraryItems
from genre.genre import Genre
from library_user.library_user import LibraryUser
from borrower_status.borrower_status import BorrowerStatus


def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        lib_items = LibraryItems(76434, "The Girl who Cried Seven Dwarfs", "Snow Black", Genre.NON_FICTION, True)

    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.
    
        print(f"Item Id: {lib_items.item_id}"
        +f"\nTitle: {lib_items.title}"
        +f"\nAuthor: {lib_items.author}"
        +f"\nGenre: {lib_items.genre.name.replace('_', ' ').title()}"
        +f"\nIs Borrowed: {lib_items.is_borrowed}")

    except Exception as e:
        print("Error: {e}")

    try:
        lib_user = LibraryUser(1234, "Frank", "frank@gmail.com", BorrowerStatus.ACTIVE)

        print(f"User Id: {lib_user.user_id}"
        +f"\nName: {lib_user.name}"
        +f"\nEmail: {lib_user.email}"
        +f"\nBorrower Status: {lib_user.borrower_status.name.title()}")

    except Exception as e:
        print("Error: {e}")
        

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        invalid_lib_item = LibraryItems(7434,"", "Snow Black", Genre.NON_FICTION, True)
    except:
        ValueError("Title cannot be blank.")
            

    # Invoking borrow item methods
    try:
        lib_user = LibraryUser(user_id=1234, name="Frank", email="frank@gmail.com", borrower_status=BorrowerStatus.ACTIVE)
        
        method_result = lib_user.borrow_item()
        print(method_result)
    except ValueError as e:
        print(e)

    # Invoking return item methods 
    try:
        lib_user = LibraryUser(user_id=1234, name="Frank", email="frank@gmail.com", borrower_status=BorrowerStatus.DELINQUENT)

        method_result = lib_user.return_item()
        print(method_result)
    except ValueError as e:
        print(e)

    # One or more invalid inputs
    try:
        lib_user = LibraryUser("1234", "Frank", "frank@gmail.com", BorrowerStatus.ACTIVE)
    except:
        ValueError("User ID is non-numeric.")

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

    user_input = input("Enter a command to run: ")
    os.system(user_input)

    eval(input("Enter an expression to evaluate: "))


if __name__ == "__main__":
    main()
