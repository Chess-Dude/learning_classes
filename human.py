class Human:
    """
    origin, organs, hair_color
    """
    def __init__(self, origin, organs, hair_color):       
        self.origin = origin
        self.organs = organs
        self.hair_color = hair_color
        print("Identifying Human")

    def __str__(self):       
        return ("This human is from %s, with %d organs, and %s hair" %(self.origin,self.organs,self.hair_color))

    def breathe(self):
        """
        """
        pass

    def eat(self):
        """
        """
        pass

    def drink(self):
        """
        """
        pass


