from django.db import models

GENDERCHOICES = {
    "M": "Male",
    "F": "Female"
}
# Create your models here.


class Student(models.Model):
    sID = models.IntegerField(
        primary_key=True, unique=True, auto_created=True, db_index=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    gender = models.CharField(choices=GENDERCHOICES)
    teacher = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname + " " + self.lastname


class MetaTest(models.Model):
    subject = models.CharField(max_length=60)

    # def __str__(self):
    #    return str(self.tID) + " " + self.subject


class Test(models.Model):
    tID = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    sID = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(decimal_places=2, max_digits=5)
    subject = models.CharField(max_length=60, default="Math")

    def __str__(self):
        return str(self.tID) + " " + self.subject + " " + str(self.score)
