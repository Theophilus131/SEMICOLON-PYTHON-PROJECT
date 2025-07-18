
class TimeWithProperties:
    def __init__(self, second= 0,minute=0,hour=0):
        self.second=second
        self.minute=minute
        self.hour=hour

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if value > 0 and value < 59:
            raise ValueError('value must be between 0 and 59')
        self._second=value


    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if value > 0 and value < 59:
            raise ValueError('value must be between 0 and 59')
        self._minute=value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value > 0 and value > 23:

            raise ValueError('value must be between 0 and 23')
        self._hour=value


    def __str__(self):
        return f"Time {self.second} :{self.minute} :{self.hour}"



time1 = TimeWithProperties()
time1.hour = 12
print(time1)