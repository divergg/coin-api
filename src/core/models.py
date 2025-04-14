from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _




class User(AbstractUser):
    """Extended User class with specific fields for the app."""

    coins = models.IntegerField(default=0, null=True, blank=True, help_text='coins awarded to the user')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class ScheduledReward(models.Model):

    execute_at = models.DateTimeField(default=None, help_text='execution time')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward')
    amount = models.IntegerField(default=0)


class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='log')
    amount = models.IntegerField(default=0)
    given_at = models.DateTimeField(auto_now_add=True)
