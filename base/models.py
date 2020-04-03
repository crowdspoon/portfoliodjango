from django.db import models


class Projectss(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    link_git = models.CharField(max_length=200)
    link_demo = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name
