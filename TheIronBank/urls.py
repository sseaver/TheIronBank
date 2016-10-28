"""TheIronBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import (IndexView, UserCreateView, TransactionListAPIView, TransactionDetailUpdateDestroyAPIView,
                       ProfileView, TransactionCreateView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url('^accounts/profile/$', ProfileView.as_view(), name="profile_view"),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^transactions/create/$', TransactionCreateView.as_view(), name="transaction_create_view"),
    url(r'^api/transactions/$', TransactionListAPIView.as_view(), name="transaction_list_api_view"),
    url(r'^api/transactions/(?P<pk>\d+)/$', TransactionDetailUpdateDestroyAPIView,
        name="transaction_detail_update_destroy_api_view"),
]
