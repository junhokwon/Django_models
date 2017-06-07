from django.db import models


class CommonInfo2(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ('-name',)
        db_table = 'django_models_mti_commoninfo2'


class Student2(CommonInfo2):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return "Homegroup {}\'s student ({},{})".format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table ='django_models_mti_student2'


class Teacher2(CommonInfo2):
    classes = models.CharField(max_length=20)

    def __str__(self):
        return 'class {} \'s teacher ({},({})'.format(
            self.classes,
            self.name,
            self.age
        )

    class Meta:
        db_table = 'django_models_mti_teacher2'

