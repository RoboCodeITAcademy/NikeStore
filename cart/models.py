from django.db import models
from shop.models import Product

# Create your models here.
class CartProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_products')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.product.name)

class Cart(models.Model):
    products = models.ManyToManyField(CartProduct)
    total_quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    def add(self,product_id, qty):
        product = Product.objects.get(id=product_id)
        price = product.price * int(qty)
        self.products.create(
            product=product,
            quantity=qty,
            price=price,
            )
        self.total_quantity += int(qty)
        self.total_price += price
        self.save()
        self.save()
        return True

    def __str__(self):
        return f"{self.total_quantity}"