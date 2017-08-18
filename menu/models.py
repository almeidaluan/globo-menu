from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
class Menu(models.Model):
    menu = models.CharField('Menu', max_length=150)

    def __str__(self):
        return self.menu

class Item(MPTTModel):
    label = models.CharField('Item',max_length=150)
    url = models.CharField('Link',max_length=150)
    parent = TreeForeignKey('self',blank=True,null=True)
    fkmenu = models.ForeignKey(Menu)

    def __str__(self):
        return self.label

    def getChildren(self):
        children = Item.objects.filter(parent_id=self)
        return children
