from django.db import models

# Create your models here.
class Setting(models.Model):
    c_name = models.CharField(max_length=250, unique= True)
    c_email = models.CharField(max_length=250, unique= True)
    c_email1 = models.CharField(max_length=250, null=True, blank=True)
    c_email2 = models.CharField(max_length=250, null=True, blank=True)
    c_phone = models.CharField(max_length=250)
    c_phone1 = models.CharField(max_length=250, null=True, blank=True)
    c_phone2 = models.CharField(max_length=250, null=True, blank=True)
    c_address = models.CharField(max_length=250)
    c_logo = models.ImageField(upload_to='logo', blank=True, null=True)
    c_meta_title = models.TextField()
    c_meta_description = models.TextField()
    
    def __str__(self):
        return self.c_name
    
    
class Attribute(models.Model):
    attribute_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.attribute_name
    
    
class AttributeValue (models.Model):
    attribute_value = models.CharField(max_length=250, unique= True)
    attribute_id = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.attribute_value
    
    
    
class Category(models.Model):
     category_name = models.CharField(max_length=250, unique=True)
     
     def __str__(self):
         return self.category_name
     
     
     
class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_slug = models.SlugField(max_length= 255, unique= True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    s_price = models.IntegerField(default=0)
    m_price = models.IntegerField(default=0)
    c_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='products')
    
    def __str__(self):
        return self.product_name
    

class ProductImage(models.Model):
    product_image_name = models.ImageField(upload_to= 'product/images')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
    
class ProductAttribute(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_value_id = models.ManyToManyField(AttributeValue)