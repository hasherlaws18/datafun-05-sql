CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    year_born INTEGER
);

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    year_published INTEGER,
    author_id TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

