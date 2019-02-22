from django.db import models

# Create your models here.


# class UserRegister(models.Model):
#     username = models.CharField(max_length=250)
#     email = models.CharField(max_length=250)
#     password = models.CharField(max_length=15)
#     reenter_password = models.CharField(max_length=15)
#
#     def __str__(self):
#         return self.username + "-" + self.email + "-" + self.password
#
#
# class UserSignup(models.Model):
#     username = models.CharField(max_length=250)
#     password = models.CharField(max_length=15)
#
#     def __str__(self):
#         return self.username + "-" + self.password


class UserLoginAndRegister(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username + "-" + self.email + "-" + self.password
