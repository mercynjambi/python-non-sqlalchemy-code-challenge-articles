  

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters long.")
        self._author = author
        self._magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles[:]

    @property
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    @property
    def topic_areas(self):
        magazines = self.magazines
        if magazines:
            return list(set(magazine.category for magazine in magazines))
        else:
            return None  # Return None when there are no topic areas

    # Disable setting the name property to enforce immutability
    @name.setter
    def name(self, new_name):
        raise AttributeError("Name attribute cannot be modified.")


class Magazine:
    def __init__(self, name, category):
        # Validate the initial name and category
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters long.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Validate the new name
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters long.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        # Validate the new category
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    @property
    def articles(self):
        return self._articles[:]

    @property
    def contributors(self):
        return list(set(article.author for article in self._articles))

    @property
    def article_titles(self):
        if not self._articles:
            return None  # Return None when there are no articles
        return [article.title for article in self._articles]

    @property
    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        
        if contributing_authors:
            return contributing_authors
        else:
            return None  # Return None when there are no contributing authors

    @classmethod
    def top_publisher(cls, magazines):
        if not magazines:
            return None
        return max(magazines, key=lambda magazine: len(magazine.articles))
