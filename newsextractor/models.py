from django.db import models
from django import forms
from django.urls import reverse


class NewsArticle(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.CharField(max_length=1000, null=True)
    date_posted = models.DateField(null=True)
    fake_status = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"Title: {self.title}, Author: {self.content}, "
            f"date posted: {self.date_posted}, content: {self.content},"
            f"status: {self.fake_status}"
        )

    def get_absolute_url(self):
        return reverse("newsarticles-detail", kwargs={"pk": self.pk})
