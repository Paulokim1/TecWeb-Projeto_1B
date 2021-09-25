from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.tag}"


class Note(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.id}. {self.title}"
