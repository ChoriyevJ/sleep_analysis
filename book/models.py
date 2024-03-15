from django.db import models


from utils import BaseModel


class Slot(BaseModel):

    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE,
                                related_name='slots')
    from_time = models.TimeField()
    to_time = models.TimeField()
    date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=False)


