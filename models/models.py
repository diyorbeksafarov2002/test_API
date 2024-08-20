import uuid

from django.db import models

class SectionModels(models.Model):
    name = models.CharField(max_length=255)

class QuestionModels(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    section = models.ForeignKey(SectionModels, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)


    def __str__(self):
        return self.question