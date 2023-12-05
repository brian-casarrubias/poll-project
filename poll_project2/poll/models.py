from django.db import models
from django.urls import reverse

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.question}'
    
    
    def get_absolute_url(self):
	#return full path as a string
        return reverse('poll-create')

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, editable=True)

    choice_text1 = models.CharField(max_length=150)
    choice_text2 = models.CharField(max_length=150)

    choice_text1_value = models.IntegerField(default=0)
    choice_text2_value = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.question}'
    

    def get_absolute_url(self):
        return reverse('poll-page', kwargs={'pk':self.pk})