# Константы
diskette_size_mb = 1.44
diskette_size_bytes = diskette_size_mb * 1024 * 1024


pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4


book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char


num_books_on_diskette = int(diskette_size_bytes // book_size_bytes)


print(f"Количество книг, помещающихся на дискету: {num_books_on_diskette}")


