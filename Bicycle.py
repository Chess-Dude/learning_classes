class Bicycle:
    """
    """
    def __init__(self, bike_type, max_speed, Number_of_gears, size):
        self.bike_type = bike_type
        self.max_speed = max_speed
        self.Number_of_gears = Number_of_gears
        self.size = size
        print("Identifying Bicycle")

    
    def __str__(self):       
        return ("This bike is a %s , with %d as its max speed, and has %d gears, The bike's size is a %s" %(self.bike_type,
                                                                                                            self.max_speed,
                                                                                                            self.Number_of_gears,
                                                                                                            self.size))


    def transports_humans():
        """
        """
        pass


    def competitive_racing():
        """
        """
        pass


    def recreational_activities():
        """
        """
        pass


    