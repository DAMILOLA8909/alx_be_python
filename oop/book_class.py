#!/usr/bin/env python3

class Book:
    """
    A class representing a book with title, author, and publication year.
    It implements __init__, __str__, __repr__, and __del__ methods.
    """

    def __init__(self, title, author, year):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.") # Added to show initialization

    def __str__(self):
        """
        Returns a human-readable string representation of the Book object.
        Used by print() and str().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the Book object,
        often used for debugging or recreating the object.
        Used by repr().
        """
        # Note: Using repr() on strings ensures quotes are included in the output
        return f"Book({repr(self.title)}, {repr(self.author)}, {self.year})"

    def __del__(self):
        """
        The destructor method, called when the instance is about to be destroyed.
        """
        print(f"Deleting {self.title}")

# The following structure is necessary to run the provided test code
def main():
    """
    Main function to demonstrate the Book class methods.
    """
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method (used by print)
    print(my_book)

    # Demonstrating the __repr__ method
    print(repr(my_book))

    # Deleting a book instance to trigger __del__
    # This explicit call triggers the destructor immediately for demonstration
    del my_book
    
    # Note: If 'del my_book' wasn't used, __del__ would still be called 
    # when the object's reference count dropped to zero (usually at program exit).

if __name__ == "__main__":
    main()