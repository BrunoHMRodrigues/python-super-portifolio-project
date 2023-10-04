from django.db import models
from django.core.validators import MaxLengthValidator, URLValidator


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    github = models.URLField(
        validators=[
            MaxLengthValidator(limit_value=500), URLValidator()
        ],
        blank=False,
    )
    linkedin = models.URLField(
        validators=[
            MaxLengthValidator(limit_value=500), URLValidator()
        ],
        blank=False
    )
    bio = models.TextField(
        validators=[MaxLengthValidator(limit_value=500)], blank=False
    )

    def __str__(self):
        return self.name
