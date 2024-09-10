class Truck:
    def __init__(self):
        self.packages_on_board = []
        self.departure_time = None
        self.time = None
        self.capacity = 16
        self.avg_speed = 18
        self.mileage = 0
        self.next_package = None
        self.location = '4001 S 700 E'

    def __str__(self):
        return f"Packages on board: {self.packages_on_board}\nDeparture time: {self.departure_time}\nCapacity: {self.capacity}\nAvg speed: {self.avg_speed}\nMileage: {self.mileage}\nNext stop: {self.next_stop}"

    def load(self, packages, departure_time):
        self.packages_on_board = packages
        self.departure_time = departure_time

    def deliver(self, package_id):
        self.packages_on_board.remove(package_id)
