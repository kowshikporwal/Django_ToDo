from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# from django import forms
class Label(models.Model):
    label_title = models.CharField(max_length=20, unique=True, help_text="Enter a Todo label(e.g.Work,Groceries etc.)")

    def get_absolute_url(self):
        return reverse('todo:label_details', kwargs={'name': self.label_title})

    def __str__(self):
        return self.label_title


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(help_text="Enter the description of todo")
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('todo:todo_details', kwargs={'pk': self.id})

    def __str__(self):
        return self.title + ' - ' + self.label.label_title


'''class TodoForms(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title''text','label','created_at']'''