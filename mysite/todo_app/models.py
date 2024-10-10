from django.db import models

# Create your models here.

"""
Ta sẽ sử dụng ORM trong django để ánh xạ những class được tạo ra trong models.py thành 1 bảng trong database.
"""

class Task (models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

