from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    distributor = models.PositiveSmallIntegerField(default=0)

class Language(models.Model):
    name = models.CharField(max_length=20)

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

class ExerciseType(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

class WordListQuestion(models.Model):
    native = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

class SentenceStructureQuestion(models.Model):
    native = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    correctOrder = models.CharField(max_length=20)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

class SentenceStructureOption(models.Model):
    value = models.CharField(max_length=100)
    tag = models.IntegerField()
    question = models.ForeignKey(SentenceStructureQuestion, on_delete=models.CASCADE)
