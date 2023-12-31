from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import TaskUser


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT)
    author = models.ForeignKey(TaskUser,
                               on_delete=models.PROTECT)
    executor = models.ForeignKey(TaskUser,
                                 on_delete=models.SET_DEFAULT,
                                 default=None,
                                 related_name="executor",
                                 null=True,
                                 blank=True)
    labels = models.ManyToManyField(Label,
                                    related_name="labels",
                                    blank=True)
