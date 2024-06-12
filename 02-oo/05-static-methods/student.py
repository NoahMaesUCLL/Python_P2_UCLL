class Duration:
    def __init__(self, *, duration_in_seconds):
        self.__duration_in_seconds = duration_in_seconds

    @staticmethod
    def from_seconds(duration):
        return Duration(duration_in_seconds=duration)
    
    @staticmethod
    def from_minutes(duration):
        return Duration(duration_in_seconds=duration * 60)
    
    @staticmethod
    def from_hours(duration):
        return Duration(duration_in_seconds=duration * 3600)
    
    @property
    def seconds(self):
        return self.__duration_in_seconds
    
    @property
    def minutes(self):
        return self.__duration_in_seconds / 60
    
    @property
    def hours(self):
        return self.__duration_in_seconds / 3600