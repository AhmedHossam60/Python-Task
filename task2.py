
records = input("Enter books and days in the format 'Book Title - Days Borrowed', separated by commas: ").split(',')

borrowed_books = {}


for record in records:
    title, days = record.strip().rsplit(' - ', 1)  
    days = int(days)  
    if title in borrowed_books:
        borrowed_books[title] += days  
    else:
        borrowed_books[title] = days  


most_borrowed = max(borrowed_books, key=borrowed_books.get)
least_borrowed = min(borrowed_books, key=borrowed_books.get)


total_days = sum(borrowed_books.values())
total_books = len(borrowed_books)
average_days = total_days / total_books


unique_titles = set(borrowed_books.keys())


sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)


print("Most borrowed book:", most_borrowed, f"({borrowed_books[most_borrowed]} days)")
print("Least borrowed book:", least_borrowed, f"({borrowed_books[least_borrowed]} days)")
print("Average borrowing days:", round(average_days, 2))
print("Unique book titles:", unique_titles)
print("Books sorted by borrowing days (descending):")
for title, days in sorted_books:
    print(f"{title}: {days} days")
