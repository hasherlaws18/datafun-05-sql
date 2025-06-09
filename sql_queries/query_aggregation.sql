-- Count how many authors there are
SELECT COUNT(first_name) AS num_authors FROM authors;

-- Average year books were published
SELECT AVG(year_published) AS avg_publish_year FROM books;

-- Total books and average publish year
SELECT COUNT(*) AS total_books, AVG(year_published) AS avg_year FROM books;
