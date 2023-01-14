CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  length INT NOT NULL
);

INSERT INTO tracks (id, title, artist, genre, length) VALUES
    (1, 'Stefania', 'KALUSH', 'UK-Rap', 180),
    (2, 'Beliver', 'Imagine Dragons', 'Pop-Rock', 205),
    (3, 'Thunder', 'Imagine Dragons', 'Pop-Rock', 208),
    (4, 'The Notebook', 'Wildways', 'Rock', 260),
    (5, 'Alone Again', 'Asking Alexandria', 'Rock', 229),
    (6, 'I`m Not Afraid', 'Tommee Profitt', 'Pop', 255),
    (7, 'In The End', 'Tommee Profitt', 'Pop', 219),
    (8, 'Dusk Till Dawn', 'ZAYN', 'Pop', 239),
    (9, 'Dangerous', 'David Guetta', 'Pop', 214),
    (10, 'Animals', 'Maroon 5', 'Pop-Rock', 231);