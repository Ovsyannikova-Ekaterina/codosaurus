from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    relation = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    time = models.IntegerField()  # duration in hours
    price = models.DecimalField(max_digits=8, decimal_places=2)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    materials = models.TextField()
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    topic = models.ForeignKey(Topic, related_name='lessons', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.topic.name} on {self.date}"

class Application(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)
    notes = models.TextField()
    parent = models.ForeignKey(Parent, related_name='applications', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='applications', on_delete=models.CASCADE)

    def __str__(self):
        return f"Application {self.id} for {self.course.name}"
