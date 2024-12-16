from database.setup import create_tables
from database.connection import get_db_connection
from models.Article import Article
from models.Author import Author
from models.Magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Create an author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid

        # Create a magazine
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid

        # Commit the author and magazine to the database
        conn.commit()

        # Create Author and Magazine instances
        author = Author(author_id, author_name)
        magazine = Magazine(magazine_id, magazine_name, magazine_category)

        # Create an Article instance
        article = Article(title=article_title, content=article_content, author=author.id, magazine=magazine.id)

        print("\n--- Data Saved Successfully ---")
        print(f"Author: {author}")
        print(f"Magazine: {magazine}")
        print(f"Article: {article}")

        # Display all magazines, authors, and articles from the database
        print("\n--- All Magazines ---")
        for magazine in Magazine.all():
            print(magazine)

        print("\n--- All Authors ---")
        for author in Author.all():
            print(author)

        print("\n--- All Articles ---")
        for article in Article.all():
            print(article)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
