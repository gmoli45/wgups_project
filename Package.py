class Package:
    def __init__(self, id, address, city, state, zip, deliveryDeadline, weight, notes):
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.notes = notes
        self.status = 'N/A'

    def __str__(self):
        return f"\nID: {self.id}\nAddress: {self.address}\nCity: {self.city}\nState: {self.state}\nZip: {self.zip}\nDelivery Deadline: {self.deliveryDeadline}\nWeight: {self.weight}\nNotes: {self.notes}\nStatus: {self.status}"
