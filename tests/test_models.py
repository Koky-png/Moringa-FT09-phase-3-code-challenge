import unittest
from models.Author import Author
from models.Magazine import Magazine
from models.Article import Article

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Today", "Technology")
        self.assertEqual(magazine.name, "Tech Today")
        self.assertEqual(magazine.category, "Technology")

    def test_article_creation(self):
        author = Author("Jane Smith")
        magazine = Magazine("Health Weekly", "Health")
        article = Article(author, magazine, "Healthy Living")
        self.assertEqual(article.title, "Healthy Living")

if __name__ == "__main__":
    unittest.main()
