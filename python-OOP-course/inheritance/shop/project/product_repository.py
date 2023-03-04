from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        match = next(
            (product for product in self.products if product.name == product_name), None
        )

        return match

    def remove(self, product_name: str):
        match = next(
            (product for product in self.products if product.name == product_name), None
        )

        if match:
            self.products.remove(match)

    def __repr__(self) -> str:
        products = "\n".join(
            f"{product.name}: {product.quantity}" for product in self.products
        )
        return products
