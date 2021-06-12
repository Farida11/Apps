from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(
        verbose_name='First name', max_length=50, blank=False)
    last_name = models.CharField(
        verbose_name='Last name', max_length=50, blank=False)
    email = models.EmailField(
        verbose_name='Email address', max_length=100, blank=False)


class Transactions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    amount = models.FloatField(
        verbose_name='Sum of a transaction', blank=False)
    date = models.DateField(verbose_name='Date', auto_now=True)
