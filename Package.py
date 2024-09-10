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
        self.departure_time = None
        self.status = 'At hub'
        self.deliveredTime = None

    def __str__(self):
        return (f"\nID: {self.id}"
                f"\nAddress: {self.address}"
                f"\nCity: {self.city}"
                f"\nState: {self.state}"
                f"\nZip: {self.zip}"
                f"\nDelivery Deadline: {self.deliveryDeadline}"
                f"\nWeight: {self.weight}"
                f"\nNotes: {self.notes}"
                f"\nStatus: {self.status}")
