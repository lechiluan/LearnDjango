from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null="true", related_name="todolist") # ForeignKey is a link to another model
    name = models.CharField(max_length=200) # CharField is a text field

    def __str__(self):
        return self.name # returns the name of the list
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # ForeignKey is a link to another model
    text = models.CharField(max_length=300) # CharField is a text field
    complete = models.BooleanField() # BooleanField is a true/false field

    def __str__(self):
        return self.text # returns the text of the item