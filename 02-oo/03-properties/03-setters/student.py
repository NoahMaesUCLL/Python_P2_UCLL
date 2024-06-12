# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if (23 < value or value < 0):
            raise ValueError()
        
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, value):
        if (59 < value or value < 0):
            raise ValueError()
        
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        if (59 < value or value < 0):
            raise ValueError()
        
        self.__seconds = value
        
    