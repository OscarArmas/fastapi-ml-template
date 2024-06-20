from application.main.domain.exceptions import PriceIsLessThanOrEqualToZero


class ProductEntity:
    def __init__(self, item_id: str, price: float):
        self.__validate_price(price)

        self.item_id = item_id
        self.price = price

    @staticmethod
    def __validate_price(price: float):
        if price <= 0:
            raise PriceIsLessThanOrEqualToZero


class ProductEntityFactory:
    @staticmethod
    def create(item_id: str, price: float) -> ProductEntity:
        return ProductEntity(item_id, price)
