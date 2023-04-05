from django.contrib import admin
from .models import ToDoList, Item # Import the ToDoList and Item models
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)