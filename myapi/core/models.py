from django.db import models

class Inventory(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    isbn = models.IntegerField()
    publisher_name = models.CharField(max_length=120)
    publisher_date = models. DateField ()
    category = models.CharField(max_length=120)
    stocks = models.IntegerField()
    # author = models.ForeignKey('Author', related_name='articles', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
