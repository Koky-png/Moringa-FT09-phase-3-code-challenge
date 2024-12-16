from database.connection import get_db_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self._id = id
        if name:
            self.name = name
        if category:
            self.category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str)  and 2 <= len(value) <= 16:
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Category cannot be empty.")
        self._category = value

    @classmethod
    def all(cls):
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM magazines')
        rows = cursor.fetchall()
        connection.close()

        return [cls(id=row['id'], name=row['name'], category=row['category']) for row in rows]

    def __repr__(self):
        return f'<Magazine: {self.name}>'
