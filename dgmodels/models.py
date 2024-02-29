from dj5.db import models, DgBaseModel
from datetime import date

class Blog(DgBaseModel):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
    class Meta(DgBaseModel.Meta):
        db_table = 'tb_blog'

class Author(DgBaseModel):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta(DgBaseModel.Meta):
        db_table = 'tb_author'

class Entry(DgBaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=256)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author, related_name='entries')
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

    class Meta(DgBaseModel.Meta):
        db_table = 'tb_entry'

class Computer(DgBaseModel):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    config = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.brand}-{self.model}'

    class Meta(DgBaseModel.Meta):
        db_table = 'tb_computer'