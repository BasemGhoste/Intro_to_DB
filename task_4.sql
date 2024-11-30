USE alx_book_store;

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = alx_book_store -- Automatically refers to the current database
  AND TABLE_NAME = 'books';