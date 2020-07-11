class book:
    def __init__(self, pages, theme, book_type):
        """
        """
        self.pages = pages
        self.theme = theme
        self.book_type = book_type
        print("Identiying Book")


    def __str__(self):       
        return ("This book has %d pages in it and it's about %s. The book has a %s" %(self.pages,
                                                                                        self.theme,
                                                                                        self.book_type))

    def to_be_read():
        """
        """
        pass
    

    def to_learn_from():
        """
        """
        pass 


    def recreational_purposes():
        """
        """
        pass