from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
# Create your models here.


ACTIONS = {
    ("W", "Withdrawal"),
    ("D", "Deposit"),
}


class Transaction(models.Model):
    user = models.ForeignKey("auth.User")
    created_time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=2, choices=ACTIONS)
    amount = models.FloatField()


class Account(models.Model):
    user = models.OneToOneField('auth.User')

    @property
    def calc_balance(self):
        return sum(Transaction.objects.filter(user=self.user).values_list("amount", flat=True))


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Account.objects.create(user=instance)


@receiver(pre_save, sender=Transaction)
def is_withdrawal(**kwargs):
    transaction = kwargs.get('instance')
    print(kwargs)
    if transaction.action == "W":
        transaction.amount = (transaction.amount * -1)
