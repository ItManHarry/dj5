from dj5.db import models, DgBaseModel
from django.db.models.functions import Coalesce
class PollManager(models.Manager):
    def with_count(self):
        return self.annotate(num_responses=Coalesce(models.Count('response'), 0))

class OpinionPoll(DgBaseModel):
    question = models.CharField(max_length=256)
    objects = PollManager()

    def __str__(self):
        return self.question

    class Meta(DgBaseModel.Meta):
        db_table = 'mg_opinion_poll'

class Response(DgBaseModel):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)

    def __str__(self):
        return f'Response of \'{self.poll.question}\''

    class Meta(DgBaseModel.Meta):
        db_table = 'mg_response'
class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')
    def editors(self):
        return self.filter(role='E')
class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)
    def authors(self):
        return self.get_queryset().authors()
    def editors(self):
        return self.get_queryset().editors()
class Person(DgBaseModel):
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=1, choices={'A': 'Author', 'E': 'Editor'})
    objects = models.Manager()
    # people = PersonManager()
    people = PersonQuerySet.as_manager()

    def __str__(self):
        return self.name
    class Meta(DgBaseModel.Meta):
        db_table = 'mg_person'
class Department(DgBaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=16)
    parent_code = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.name}({self.code})'
    class Meta(DgBaseModel.Meta):
        db_table = 'mg_department'
class DepartmentInf(DgBaseModel):
    d_name = models.CharField(max_length=128)
    d_code = models.CharField(max_length=16)
    d_parent_code = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.d_name}({self.d_code})'
    class Meta(DgBaseModel.Meta):
        db_table = 'mg_department_inf'