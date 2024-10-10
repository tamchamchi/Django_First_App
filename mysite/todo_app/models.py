from djongo import models
# Create your models here.

"""
Ta sẽ sử dụng ORM trong django để ánh xạ những class được tạo ra trong models.py thành 1 bảng trong database.

the makemigrations command: là cách để tạo ra database tables.

0001_initial.py: chứa những cái instructions cho việc tạo database structure.
"""

class Task (models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

