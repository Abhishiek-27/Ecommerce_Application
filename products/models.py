from django.db import models
from base.models import BaseModel



class Category(BaseModel):
    category_name =  models.CharField(max_length=100)
    slug = models.SlugField(unique= True, null=True, blank=True)
    category_image = models.ImageField(upload_to=  "catgories")



class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique= True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    products_descriptions = models.TimeField()



class ProductsImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="procuct_images")
    image = models.ImageField(upload_to= "product")