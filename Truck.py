class Truck:
    def __init__(self):
        self.current_driver = None
        self.packages_on_board = []
        self.departure_time = None
        self.capacity = 16
        self.avg_speed = 18
        self.mileage = 0
        self.next_stop = ''
        self.location = '4001 South 700 East'

    def __str__(self):
        return f"Current driver: {self.current_driver}\nPackages on board: {self.packages_on_board}\nDeparture time: {self.departure_time}\nCapacity: {self.capacity}\nAvg speed: {self.avg_speed}\nMileage: {self.mileage}\nNext stop: {self.next_stop}"

    def load(self, packages, driver, departure_time, first_stop):
        self.current_driver = driver
        self.packages_on_board = packages
        self.departure_time = departure_time
        self.next_stop = first_stop