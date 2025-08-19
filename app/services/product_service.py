from app.repositories.product_repo import ProductRepository
from app.schemas.product import ProductCreate

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def create_product(self, product: ProductCreate):
        # You can add business logic like price validation here
        return self.repo.create_product(product)

    def list_products(self):
        return self.repo.get_products()

    def get_product(self, product_id: int):
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise Exception("Product not found")
        return product
