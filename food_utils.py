class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ' that costs #' + str(self.price)

    def total_price(self, order_count):
        total_price = self.price * order_count
        if order_count >= 3:  # discount of 75% after purchasing 3 items
            total_price *= 0.75
        return round(total_price)
