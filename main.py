from models.book import Book
from models.ebook import EBook
from models.audiobook import AudioBook
from services.book_manager import BookManager
from services.reading_tracker import ReadingTracker
from services.progress_manager import ProgressManager
from storage.data_exporter import DataExporter
from storage.data_importer import DataImporter

def main() -> None:
    print("⇛⇛⇛⇛⇛⇛ BookBuddy CLI Mockup ⇚⇚⇚⇚⇚")

    book_manager = BookManager()
    reading_tracker = ReadingTracker(book_manager)
    exporter = DataExporter()
    importer = DataImporter()

    while True:
        print("\nMain Menu:")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Log reading progress")
        print("4. View reading progress")
        print("5. Export book data")
        print("6. Import book data")
        print("7. Exit")

        choice = input("\nEnter your choice : ")

        if choice == '1':
            print("\n--- 1. Add a New Book ---")
            print("Type: 1. Normal Book | 2. EBook | 3. AudioBook")
            book_type = input("Choose type (1-3): ")

            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")

            try:
                pages = int(input("Enter total pages: "))

                if book_type == '2':
                    file_size = input("Enter file size (example 5MB): ")
                    new_book = EBook(title, author, genre, pages, file_size)
                elif book_type == '3':
                    duration = input("Enter duration (example 10h 30m): ")
                    new_book = AudioBook(title, author, genre, pages, duration)
                else:
                    new_book = Book(title, author, genre, pages)

                book_manager.add_book(new_book)
                print(f"\nBook '{title}' added successfully!")
            except ValueError:
                print("Invalid input for pages. Must be a number.")

        elif choice == '2':
            print("\n--- Your Library ---")
            books = book_manager.list_books()
            if not books:
                print("No books in library.")
            else:
                for i, book in enumerate(books, 1):
                    b_type = book.__class__.__name__
                    print(f"{i}. {book.title} by {book.author} [{book.genre}] ({b_type}) - {book.pages} pages")

        elif choice == '3':
            print("\n--- Log Reading Progress ---")
            title = input("Enter book title: ")
            try:
                pages = int(input("Enter pages read: "))
                notes = input("Enter notes (optional): ")
                success = reading_tracker.log_reading(title, pages, notes)
                if success:
                    print("Reading log added!")
            except ValueError:
                print("Invalid input for pages.")

        elif choice == '4':
            print("\n--- Reading Progress ---")
            books = book_manager.list_books()
            if not books:
                print("No books to track.")
            else:
                summary = ProgressManager.get_reading_summary(books)
                for item in summary:
                    print(f"{item['title']} - {item['pages_read']}/{item['total_pages']} pages read ({item['progress_percent']:.1f}%)")

        elif choice == '5':
            print("\n--- Export Book Data ---")
            print("1. JSON | 2. JSON Lines (JSONL) | 3. Pickle")
            fmt = input("Choice : ")
            filename = input("Enter filename : ")

            if fmt == '1' and not filename.endswith('.json'):
                filename += '.json'
            elif fmt == '2' and not filename.endswith('.jsonl'):
                filename += '.jsonl'
            elif fmt == '3' and not filename.endswith('.pkl'):
                filename += '.pkl'

            books = book_manager.list_books()

            if fmt == '1':
                exporter.export_to_json(books, filename)
            elif fmt == '2':
                exporter.export_to_jsonl(books, filename)
            elif fmt == '3':
                exporter.export_to_pickle(books, filename)
            else:
                print("Invalid choice.")

        elif choice == '6':
            print("\n--- Import Book Data ---")
            print("1. JSON | 2. JSON Lines (JSONL) | 3. Pickle")
            fmt = input("Choice (1-3): ")
            filename = input("Enter filename: ")

            if fmt == '1' and not filename.endswith('.json'):
                filename += '.json'
            elif fmt == '2' and not filename.endswith('.jsonl'):
                filename += '.jsonl'
            elif fmt == '3' and not filename.endswith('.pkl'):
                filename += '.pkl'

            try:
                if fmt == '1':
                    imported_books = importer.import_from_json(filename)
                elif fmt == '2':
                    imported_books = importer.import_from_jsonl(filename)
                elif fmt == '3':
                    imported_books = importer.import_from_pickle(filename)
                else:
                    print("Invalid choice.")
                    imported_books = []

                for book in imported_books:
                    book_manager.add_book(book)
                if imported_books:
                    print(f"\n{len(imported_books)} books imported successfully!")
            except Exception as e:
                print(f"Error importing data: {e}")

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please select a number between 1 and 7.")

if __name__ == "__main__":
    main()