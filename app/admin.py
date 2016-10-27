from django.contrib import admin
from app.models import Account, Transaction
# Register your models here.
admin.site.register([Account, Transaction])
