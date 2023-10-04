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


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=False)
    github_url = models.URLField(
        validators=[
            MaxLengthValidator(limit_value=500), URLValidator()
        ],
        blank=False,
    )
    keyword = models.CharField(max_length=50, blank=False)
    key_skill = models.CharField(max_length=50, blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name