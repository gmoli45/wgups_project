class Package:
    def __init__(self, id, address, city, state, zip, delivery_deadline, weight, notes, status):
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return f"\nID: {self.id}\nAddress: {self.address}\nCity: {self.city}\nState: {self.state}\nZip: {self.zip}\nDelivery Deadline: {self.delivery_deadline}\nWeight: {self.weight}\nNotes: {self.notes}\nStatus: {self.status}"
