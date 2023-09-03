from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
import datetime
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from PIL import Image
import os
from datetime import date
# from .forms import UserManager


def convert_heic_to_jpg(heic_image):
    img = Image.open(heic_image)
    jpeg_path = os.path.splitext(heic_image.path)[0] + '.jpg'
    img.convert('RGB').save(jpeg_path, format='JPEG')
    return jpeg_path

class Menu(models.Model):
    name = models.CharField(max_length=30,verbose_name="Menu ady:")
    status = models.BooleanField(default=False,verbose_name="Bas sahypada gorkez:")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Menular"

class AboutUs(models.Model):
    description = models.TextField(verbose_name="Biz hakda(text):")
    phone = models.PositiveIntegerField(verbose_name="Telefon belgi(6xxxxxxx):",default=0)
    phone2 = models.PositiveIntegerField(verbose_name="Telefon belgi2(6xxxxxxx):",default=0,blank=True)
    phone3 = models.PositiveIntegerField(verbose_name="Telefon belgi3(6xxxxxxx):",default=0,blank=True)
    email = models.CharField(max_length=50,verbose_name="E-Pocta salgynyz:",default="")
    adress = models.CharField(max_length=100,verbose_name="Yerlesyan yeriniz:",default="")
    image = models.ImageField(verbose_name="Biz hakda ucin logo:",upload_to="about_us/")
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image.path.lower().endswith('.heic'):
            jpeg_path = convert_heic_to_jpg(self.image)
            self.image.path = jpeg_path
            self.image.name = os.path.basename(jpeg_path)
            super().save(update_fields=['image'])
    
    class Meta:
        verbose_name_plural = "Biz hakda"

class Category(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,verbose_name="Menu sayla:")
    name = models.CharField(max_length=30,verbose_name="Kategoriya ady:")
    status = models.BooleanField(default=False,verbose_name="Bas sahypada gorkez:")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.menu} - {self.name}"
    
    class Meta:
        verbose_name_plural = "Kategoriyalar"
    
class Banner(models.Model):
    name = models.CharField(max_length=100,verbose_name="Banner ady:")
    image = models.ImageField(upload_to="img/",verbose_name="Banner suraty:")
    link = models.CharField(max_length=1000,verbose_name="Link:")
    date = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Bannerler"
    
class Brand(models.Model):
    name = models.CharField(max_length=50,verbose_name="Brand ady:")
    image = models.ImageField(upload_to='brand/',verbose_name="Brand logo:")

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Brendler"
    
class Product(models.Model):
    productCode = models.CharField(max_length=200,verbose_name="Haryt kody:")
    productName = models.CharField(max_length=200,verbose_name="Haryt ady:")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name="Brand ady:")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Kategoriya ady:")
    description = models.TextField(verbose_name="Haryt dusundirisi:")
    price = models.FloatField(verbose_name='Haryt taze baha:')
    oldPrice = models.FloatField(verbose_name="Haryt kone baha:")
    image = models.ImageField(upload_to='product/',verbose_name="Haryt suraty:")
    status = models.BooleanField(default=False,verbose_name="Hayrt yagdayy:")
    date = models.DateTimeField(auto_now_add=True)

    def delete_with_related(self):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        self.delete()    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image.path.lower().endswith('.heic'):
            jpeg_path = convert_heic_to_jpg(self.image)
            self.image.path = jpeg_path
            self.image.name = os.path.basename(jpeg_path)
            super().save(update_fields=['image'])

    def __str__(self):
        return f"{self.productCode} - {self.productName}"
    
    @property
    def new_or_not(self):
        today = date.today()
        if self.date.date() < today:
            taze = ""
        else:
            taze = "Taze"
        return taze
    
    class Meta:
        verbose_name_plural = "Harytlar"

class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Haryt saylan:')
    images = models.ImageField(upload_to='product/',verbose_name="Suratlary saylan:")

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image.path.lower().endswith('.heic'):
            jpeg_path = convert_heic_to_jpg(self.images)
            self.image.path = jpeg_path
            self.image.name = os.path.basename(jpeg_path)
            super().save(update_fields=['image'])

    class Meta:
        verbose_name_plural = "Haryt Suratlary"

# class Color(models.Model):
#     colorCode = models.CharField(max_length=6,verbose_name='Renk kody:')
#     colorName = models.CharField(max_length=200,verbose_name='Renk ady:')
#     def __str__(self):
#         return f"{self.colorName} - {self.colorCode}"
    
# class ProductColor(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
#     colorInfo = models.ForeignKey(Color,on_delete=models.CASCADE,verbose_name="Renk saylan:")
#     colorImage = models.ImageField(upload_to='product/',verbose_name="Suratlary saylan:")
    
#     def delete(self, *args, **kwargs):
#         if self.image:
#             if os.path.exists(self.image.path):
#                 os.remove(self.image.path)
#         super().delete(*args, **kwargs)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if self.image.path.lower().endswith('.heic'):
#             jpeg_path = convert_heic_to_jpg(self.colorImage)
#             self.image.path = jpeg_path
#             self.image.name = os.path.basename(jpeg_path)
#             super().save(update_fields=['image'])
    
# class SizeType(models.Model):
#     name = models.CharField(max_length=20,verbose_name='Olceg gornusinin ady(Metr,Ram,Olceg):')
#     def __str__(self):
#         return self.name

# class Size(models.Model):
#     sizeType = models.ForeignKey(SizeType,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Olceg gornusi:')
#     size = models.CharField(max_length=10,verbose_name='Olcegi yazyn:')

class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE,verbose_name="Teswir yazan:")
    product = models.ForeignKey(Product, models.CASCADE,verbose_name="Teswir yazylan haryt:")
    comment = models.TextField(max_length=250,verbose_name="Teswir:")
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "Teswirler"
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    add_time = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.quantity * self.product.price
    
    class Meta:
        verbose_name_plural = "Sebetler"
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Halananlar"

class City(models.Model):
    name = models.CharField(max_length=50,verbose_name="Saher ady:")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Şäherler"

class Etrap(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name="Etrap ady:")
    toleg = models.PositiveIntegerField(default=0,verbose_name="Yol tolegi:")
    def __str__(self):
        return f"{self.city}-{self.name}"
    class Meta:
        verbose_name_plural = "Etraplar"
    
PAYMENT_CHOICES = (
    ('NAGT TÖLEG','NAGT TÖLEG'),
    ('KARTDAN TÖLEG','KARTDAN TÖLEG'),
)

STATUS_CHOICES = (
    ('Kabul edildi','Kabul edildi'),
    ('Taýýarlanýar','Taýýarlanýar'),
    ('Ugradyldy','Ugradyldy'),
    ('Gowşuruldy','Gowşuruldy'),
    ('Kabul edilmedi','Kabul edilmedi'),
    ('Garaşylýar','Garaşylýar'),
)

class Order(models.Model):
    productCode = models.CharField(max_length=100000,default='')
    productBrand = models.CharField(max_length=100000,default='')
    product = models.CharField(max_length=100000,default='')
    productDesc = models.CharField(max_length=100000,default='')
    productImage = models.CharField(max_length=100000,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    total = models.CharField(max_length=1000000,default='')
    adress = models.TextField(default='')
    payment_choices = models.CharField(max_length=20,choices=PAYMENT_CHOICES,default='NAGT TÖLEG')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Garaşylýar')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product
    
    @property
    def Days_till(self):
        today = datetime.date.today()
        # days_till = self.date.date() - today 
        days_till = self.date
        # days_till_stripped = str(days_till).replace('г.','ýyl')[0]
        return days_till
    
    class Meta:
        verbose_name_plural = "Sargytlar"

class Adress(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    city = models.ForeignKey(City,default=0,on_delete=models.CASCADE)
    city_etrap = models.ForeignKey(Etrap,default=0,on_delete=models.CASCADE)
    adress = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Salgylar"

class Help(models.Model):
    question = models.CharField(max_length=255,verbose_name="Kop soralyan sorag(Bu sahypa name is etyar?):")
    answer = models.TextField(verbose_name="Soragy jogaby:")
    class Meta:
        verbose_name_plural = "Kömek(Soraglar üçin)"

class ExchangeCondition(models.Model):
    condition = models.TextField(verbose_name="Şert ýazyň:")
    class Meta:
        verbose_name_plural = "Çalşyp bermek şertleri"
    
class Contact(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,verbose_name="Ady:")
    lastName = models.CharField(max_length=255,verbose_name="Familýasy:")
    message = models.TextField(verbose_name="Haty:")