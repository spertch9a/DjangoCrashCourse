from django.db import models

# Create your models here.
#a model is the representation of our database schema

#a model to represendt what a at todo is, it has a name and a due date

class Todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    
    def __str__(self):
        return self.name