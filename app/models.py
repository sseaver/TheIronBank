from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


ACTIONS = {
    ("W", "withdrawal"),
    ("D", "deposit"),
}


class Transaction(models.Model):
    user = models.ForeignKey("auth.User")
    created_time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=2, choices=ACTIONS)
    amount = models.FloatField()


class Account(models.Model):
    user = models.ForeignKey('auth.User')
    transactions = models.ManyToManyField(Transaction)

    @property
    def calc_balance(self):
        return sum(self.transactions.all().value_list("amount", flat=True))


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Account.objects.create(user=instance)
