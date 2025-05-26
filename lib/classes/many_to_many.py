class Article:
  
    _all_articles = []

    def __init__(self, author, magazine, title):
        
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")
        
        if not isinstance(title, str):
            raise TypeError("Title must be of type str.")
        if not (5 <= len(title.strip()) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")


        self._author = author
        self._magazine = magazine
        self._title = title

        
        Article._all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):        
        if hasattr(self, '_title'):
            raise AttributeError("Cannot change title after the article is instantiated.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):        
        if not isinstance(value, Author):
            raise TypeError("Author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):        
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")
        self._magazine = value

    @classmethod
    def all(cls):        
        return cls._all_articles

        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str.")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str.")
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change name after author is instantiated.")
        self._name = value


    def articles(self):
        return [article for article in Article._all_articles if article.author == self]
        

    def magazines(self):
        return list(set(article.magazine for article in Article._all_articles if article.author == self))  
        

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str.")
        if not (2 <= len(value.strip()) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type str.")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value.strip()


    def article_titles(self):
        titles = [article.title for article in Article.all() if article.magazine == self]
        return titles if titles else None

    
    def articles(self):
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))
   
    def contributing_authors(self):
        author_counts = {}
        for article in Article.all():
            if article.magazine == self:
                author = article.author
                author_counts[author] = author_counts.get(author, 0) + 1
    
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None