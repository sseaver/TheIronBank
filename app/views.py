from django.shortcuts import render
from app.models import Account, Transaction
from app.serializers import TransactionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
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


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ("action", "amount")
    success_url = reverse_lazy("profile_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class TransactionListAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class TransactionDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
