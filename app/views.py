from django.shortcuts import render
from app.models import Account, Transaction
from app.serializers import TransactionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views import View
# Create your views here.


class IndexView(View):
    pass


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class TransactionListAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class TransactionDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
