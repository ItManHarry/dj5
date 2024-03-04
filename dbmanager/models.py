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
