from django.db import models
import datetime
from datetime import date
from django.utils import timezone
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    def __str__(self):
        return self.question_text
    @property
    def was_published_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
'''
One to many relationship
'''
class Reporter(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=24)
    email = models.CharField(max_length=128)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
class Publication(models.Model):
    name = models.CharField(max_length=128)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
class Article(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    pub_date = models.DateField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    publications = models.ManyToManyField(Publication)
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ['headline']
'''
Many to many relationship
'''
import uuid
class BaseModel(models.Model):
    class Meta:
        abstract = True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

class Person(BaseModel):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
class Group(BaseModel):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(Person, through='MemberShip')

    def __str__(self):
        return self.name
class MemberShip(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.person}({self.group})'
'''
One to one relationship
'''
class Place(BaseModel):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} the place'

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=128, null=True)
    serves_hot_dog = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Restaurant {self.name} at the {self.place.name}'

class Waiter(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    def __str__(self):
        return f'waiter {self.name} at restaurant {self.restaurant}'
'''
Proxy
'''
class Employee(BaseModel):
    name = models.CharField(max_length=64)
    birthday = models.DateField(null=True)
    email = models.CharField(max_length=128)
    def __str__(self):
        return self.name
class ProxyEmployee1(Employee):
    class Meta:
        proxy = True
        ordering = ['-name']
    @property
    def age(self):
        return (date.today() - self.birthday).days // 365

class ProxyEmployee2(Employee):
    class Meta:
        proxy = True
        ordering = ['name']