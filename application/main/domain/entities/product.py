from application.main.domain.exceptions import PriceIsLessThanOrEqualToZero


class ProductEntity:

    def __init__(self, name: str, price: float):
        self.__validate_price(price)

        self.name = name
        self.price = price

    @staticmethod
    def __validate_price(price: float):
        if price <= 0:
            raise PriceIsLessThanOrEqualToZero


class ProductEntityFactory:

    @staticmethod
    def create(name: str, price: float) -> ProductEntity:
        return ProductEntity(name, price)
