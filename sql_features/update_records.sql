UPDATE books
SET year_published = 1954
WHERE title = 'The Fellowship of the Ring';

UPDATE authors
SET year_born = 1892
WHERE last_name = 'Tolkien' AND first_name = 'J.R.R.';
