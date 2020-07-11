class Robot:

    """
    smartness, processing_power, sensors
    """

    def __init__(self, smartness, processing_power, sensors):
        self.smartness = smartness
        self.processing_power = processing_power
        self.sensors = sensors
        print("Robot is being manufactured")

    def __str__(self):       
        return ("This robot has a IQ of %d, with %d processing power, and %d sensors" %(self.smartness,
                                                                                        self.processing_power,
                                                                                        self.sensors))

    def lifting_heavy_items(self):
        """
        """
        pass

    def detects(self):
        """
        """
        pass

    def assiting_humans(self):
        """
        """
        pass