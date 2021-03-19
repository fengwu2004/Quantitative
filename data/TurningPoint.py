class TurningPoint(object):

    value: float

    index: int

    date:int

    upward:bool

    def __init__(self, i:int, date:int, value:float, upward:bool):

        super().__init__()

        self.index = i

        self.date = date

        self.value = value

        self.upward = upward

    def __str__(self):

        return 'i = ' + str(self.index) + ', ' + ' date = ' + str(self.date) + ', ' + 'value = ' + str(self.value)