class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self._author.add_articles(self)
        self.magazine.add_article(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Set the title while ensuring immutability (it cannot be changed once set)
        if self._title is not None:
            raise AttributeError("Title cannot be changed once set.")  # Ensure immutability
        # Ensure the title is a string between 5 and 50 characters
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
         # Ensure that the author is an instance of the Author class
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an instance of the Author")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        # Ensure that the magazine is an instance of the Magazine class
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be an instance of the Magazine")


        
# class Author:
#     def __init__(self, name):
#         self.name = name

#     def articles(self):
#         pass

#     def magazines(self):
#         pass

#     def add_article(self, magazine, title):
#         pass

#     def topic_areas(self):
#         pass

# class Magazine:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     def articles(self):
#         pass

#     def contributors(self):
#         pass

#     def article_titles(self):
#         pass

#     def contributing_authors(self):
#         pass


