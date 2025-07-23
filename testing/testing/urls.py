"""
URL configuration for testing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
import django.contrib.admin as django_admin
from django.conf.urls.static import static
from django.conf import Settings


from myapp.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('admin/', django_admin.site.urls),
    path('admin/', django_admin.site.urls),




    
    # path('register/',register,name="register")
    #path('login/',login_page, name='login'),
    #path('dashboard/', lambda request: render(request, 'dashboard.html')),
    #path('login/',login_page,name="login_page"),
    
    path("login/",login_views,name="login_views"),
    path("logout/",logout,name="logout"),

    path('dashboard/',dashboard,name='dashboard'),


    path('category_view/',category_view,name='category_view'),
    path('category_viewdata/',category_viewdata,name='category_viewdata'),


    path('catCreate/',catCreate,name="catCreate"),
    path('catList/',catList,name="tablelist"),
    path('catEdit/<int:id>',catEdit,name="catEdit"),
    path('catDelete/<int:id>/', catDelete, name='catDelete'),
    path('catImage/',catImage,name="catImage"),

    




    path('article_view/',article_view,name='article_view'),   #article table
    path('article_viewdata/',articale_create,name='article_viewdata'),   #article form
    path('article_delete/<int:id>/',articale_delete,name="articale_delete"), #article delete
    path('articale_Edit/<int:id>/',articale_Edit,name="articale_Edit"),  #article edit

    # path('articale_create/',articale_create,name='articale_create'),




    




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

