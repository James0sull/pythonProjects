class Order:

    def __init__(self, item, qty, price):
        self.item = item
        self.qty = qty
        self.price = price
        self.total = self.qty * self.price