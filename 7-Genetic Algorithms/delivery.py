class Delivery:
    def __init__(self, orders):
        self.orders = orders

    def deliver_item(self, item):
        if item in self.orders.keys() and self.orders[item] > 0:
            self.orders[item] -= 1
            if self.orders[item] == 0:
                del self.orders[item]
            return True
        return False
