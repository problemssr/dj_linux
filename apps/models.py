from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=10)
    age = models.IntegerField(verbose_name="年龄")

    def __str__(self):
        return self.name


class AManager(models.Manager):
    def get_queryset(self):
        return super(AManager, self).get_queryset()


class People(models.Model):
    p_name = models.CharField(max_length=16, unique=True, db_column="name")
    p_age = models.IntegerField(default=18, db_column="age")
    p_sex = models.BooleanField(default=False, db_column="sex")

    # a=models.Manager()
    a = AManager()

    class Meta:
        db_table = 'People'
        ordering = ['id']
