from dj5.db import models, DgBaseModel
from datetime import date
class Author(DgBaseModel):
    class Meta(DgBaseModel.Meta):
        db_table = 'biz_author'
    name = models.CharField(max_length=128)
    age = models.IntegerField(default=10)

    def __str__(self):
        return self.name
class Publisher(DgBaseModel):
    class Meta(DgBaseModel.Meta):
        db_table = 'biz_publisher'
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Book(DgBaseModel):
    class Meta(DgBaseModel.Meta):
        db_table = 'biz_book'
        ordering = ['name']
    name = models.CharField(max_length=128)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return self.name

class Store(DgBaseModel):
    class Meta(DgBaseModel.Meta):
        db_table = 'biz_store'
    name = models.CharField(max_length=128)
    books = models.ManyToManyField(Book, related_name='stores')

    def __str__(self):
        return self.name