""" models """
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """
    This define category
    """
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
                create SEO-friendly url from our app url patterns
        """
        return reverse('app:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """
    This is product description
    """
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:product_detail', args=[self.id, self.slug])


class Cart(models.Model):
    """
    Cart of a databases
    """
    cart = models.ForeignKey(
        Product, related_name='carts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """ User registration model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, null=True)
    contact = models.CharField(max_length=11)
    postal_code = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
