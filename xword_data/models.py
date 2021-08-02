from django.db import models

# Create your models here.
class puzzle(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(blank=False)
    byline = models.CharField(max_length=250, blank=False)
    publisher = models.CharField(max_length=25, blank=False)

class entry(models.Model):
    entry_text = models.CharField(max_length=50, blank=False, unique=True)

class clue(models.Model):
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
    puzzle = models.ForeignKey('Puzzle', on_delete=models.CASCADE)
    clue_text = models.CharField(max_length=500, blank=False)
    theme = models.BooleanField(default=False)
