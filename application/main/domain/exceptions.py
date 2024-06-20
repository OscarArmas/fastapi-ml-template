class InvalidPrice(Exception):
    def __init__(self):
        super().__init__("The price is not a valid number")


class PriceIsLessThanOrEqualToZero(Exception):
    def __init__(self):
        super().__init__("The price is less than or equal to zero")


class ItemNotFound(Exception):
    def __init__(self, item_id: str):
        self.message = f"item_id: {item_id} not found"
        self.status_code = 404
        super().__init__(self.message)
