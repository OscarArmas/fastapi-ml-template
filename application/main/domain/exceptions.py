class InvalidPrice(Exception):
    def __init__(self):
        super().__init__("The price is not a valid number")


class PriceIsLessThanOrEqualToZero(Exception):
    def __init__(self):
        super().__init__("The price is less than or equal to zero")
