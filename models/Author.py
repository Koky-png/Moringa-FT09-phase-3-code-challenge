from database.connection import get_db_connection

class Author:
    def __init__(self, author_id, name):
        self._id = author_id  # Private attribute
        self.name = name

    @property
    def id(self):  # Public property to access `id`
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
