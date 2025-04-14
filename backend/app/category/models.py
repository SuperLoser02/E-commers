from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """
    Modelo que representa la categorias de los productos existente
    
    Atributos:
        category_name (Charfild|varchar): Nombre UNICO de la categoria (max 20 
        caracteres)
        description (CharField|varchar): Descripcion OPCIONAL de la categoria
        (max 255 caracteres)
        slug (CharField|varchar): 
    """
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug =  models.CharField(max_length=100, unique=True)
    cat_image =  models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name