"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from firstapp import views
from Users import views as user_views
from firstapp.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.home, name="home_page"),
    path('books/',views.show_active_books, name="all_active_books"),
    path('update1/<int:id>/',views.update_book, name="update_book"),
    path( 'delete1/<int:pk>/',views.delete_book, name="delete_book"),
    path('soft-delete/<int:pk>/',views.soft_delete_book,name="soft_delete_book"),
    path('inactive-books/',views.show_inactive_books,name="all_inactive_books"),
    path('restore-book/<int:pk>/',views.restore_book,name="restore_book"),
    path('book-form',views.book_form,name="book_form"),
    path('sibtc-form',views.sibtc,name="sibtc"),
    path('register/',user_views.register_request,name="register"),
    path('login/',user_views.login_request,name="login_user"),
    path('logout/',user_views.logout_request,name="logout_user"),
    path('create-csv/',views.create_csv,name="create_csv"),
    path('upload-csv/',views.upload_csv,name="upload_csv"),
    path('index/',views.index,name="index"),
    path('cbv-create-book/',views.BookCreate.as_view(),name="BookCreate"),
    path('retrieve/',views.BookRetrieve.as_view(),name="BookRetrieve"),
    path('retrieve/<int:pk>/',views.BookDetail.as_view(),name="BookDetail"),
    path('update/<int:pk>/',views.BookUpdate.as_view(),name="BookUpdate"),
    path('delete/<int:pk>/',views.BookDelete.as_view(),name="BookDelete")
]
