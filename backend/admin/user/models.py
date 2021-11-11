from django.db import models

# Create your models here.


class UserVo(models.Model):
    use_in_migrations = True
    user_id = models.AutoField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    name = models.TextField()
    email = models.EmailField()
    reg_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return f'[{self.pk}] {self.user_id}'