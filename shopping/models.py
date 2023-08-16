from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class shoppingItemModel(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], null=True )
    discount = models.FloatField(null=True, blank=True, default=0.0, validators=[MaxValueValidator(100)] )
    description = models.TextField()
    
    def __str__(self) :
        return self.name