from database.connection import get_db_connection


class Article:
    def __init__(self, article_id=None, title=None, content=None, author=None, magazine=None):
        self.article_id = article_id
        self.title = title
        self.content = content
        self.author = author
        self.magazine = magazine

        if self.article_id is None and self.title is not None:
            self.create_article()
        elif self.article_id is not None:
            self.load_article_data()

    @property
    def id(self):
        return self.article_id

    def create_article(self):
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (self.title, self.content, self.author, self.magazine)
        )
        self.article_id = cursor.lastrowid
        connection.commit()
        connection.close()

    def load_article_data(self):
        if self.article_id is None:
            raise ValueError("Cannot load data without an article ID.")

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            'SELECT title, content, author_id, magazine_id FROM articles WHERE id = ?',
            (self.article_id,)
        )
        row = cursor.fetchone()

        if row:
            self.title, self.content, self.author, self.magazine = row
        else:
            raise ValueError("No article found with the given ID.")

        connection.close()

    @classmethod
    def all(cls):
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM articles')
        rows = cursor.fetchall()
        connection.close()

        return [
            cls(article_id=row['id'], title=row['title'], content=row['content'], author=row['author_id'], magazine=row['magazine_id'])
            for row in rows
        ]

    def __repr__(self):
        return f"<Article: {self.title}>"


class Author:
    def __init__(self, author_id, name):
        self._id = author_id
        self.name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not (2 <= len(value) <= 50):
            raise ValueError("Name must be between 2 and 50 characters.")
        self._name = value

    @classmethod
    def all(cls):
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM authors')
        rows = cursor.fetchall()
        connection.close()

        return [cls(author_id=row['id'], name=row['name']) for row in rows]

    def __repr__(self):
        return f"<Author: {self.name}>"



   
