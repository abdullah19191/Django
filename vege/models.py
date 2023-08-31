from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_discription = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    recipe_view_counts = models.IntegerField(default=1)


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ["department"]


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id


class Student(models.Model):
    # Fields for the Student model
    department = models.ForeignKey(
        Department, related_name="depart", on_delete=models.CASCADE
    )
    student_id = models.OneToOneField(
        StudentID, related_name="studentid", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=18)
    address = models.TextField(max_length=500, default="Add Address Here")

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["first_name"]
        verbose_name = "student"
