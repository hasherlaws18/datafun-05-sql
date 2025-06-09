SELECT 
    books.title,
    books.year_published,
    authors.first_name,
    authors.last_name
FROM books
JOIN authors ON books.author_id = authors.author_id
WHERE books.year_published > 1950;
