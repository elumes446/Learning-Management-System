from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import file_size

class User(AbstractUser):
    is_admin = models.BooleanField('Is employee', default=False)
    is_teacher= models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is customer', default=False)
    def __str__(self):
        return self.username

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

class Video(models.Model):
    caption = models.CharField(max_length=5000, blank=True, null=True)
    video  = models.FileField(upload_to="video/%y", validators =[file_size])
    def __str__(self):
        return self.caption
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='books/')


class Exam(models.Model):
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    total_marks = models.PositiveIntegerField()

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    image = models.ImageField(upload_to='exam_images', blank=True, null=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)