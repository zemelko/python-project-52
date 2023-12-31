from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['status_name']
        labels = {
            'status_name': _('Name')
        }
