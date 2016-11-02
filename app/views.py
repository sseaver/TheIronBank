from django.shortcuts import render
from app.models import Account, Transaction
from app.serializers import TransactionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['login_form'] = AuthenticationForm
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class ProfileView(ListView):
    model = Transaction

    def get_context_data(self):
        context = super().get_context_data()
        context['user_transactions'] = Transaction.objects.filter(user=self.request.user)
        return context


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ("action", "amount")
    success_url = reverse_lazy("profile_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class TransactionListAPIView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class TransactionRetrieveAPIView(RetrieveAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, **kwargs):
        return Transaction.objects.filter(user=self.request.user)
