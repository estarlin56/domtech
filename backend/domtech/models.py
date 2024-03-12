from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Catalog(models.Model):
    
    class CatalogStatus(models.IntegerChoices):
        INACTIVE = 0, _('Inactive')
        ACTIVE = 1, _('Active')
        __empty__ = _('Select catalog status.') 

    class Meta:
        """Meta definition for Catalog."""
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"
        
    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=CatalogStatus.choices, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


