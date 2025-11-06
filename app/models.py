from django.db import models
 
class Student(models.Model):
    name = models.CharField(max_length=100)
    no = models.IntegerField()
    image = models.ImageField(upload_to="student_images/",blank=True,null=True)
    def __str__(self):
        return self.name
