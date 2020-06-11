"""psp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$',views.index),
    path('gxjjpt/rest/submit_user_sign_data',views.sign),
    path('gxjjpt/rest/pay_from_accout',views.withDrawal),
    path('gxjjpt/rest/goto_sign_plugin',views.autograph),
    url(r'^callback/$',views.callback),
    url(r'^signResult/$',views.signResult),
    path('gxjjpt/rest/get_contract',views.getContract),
    url(r'^withDrawalResult/$', views.withDrawalResult),

]
