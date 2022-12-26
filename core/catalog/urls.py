from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_book/', views.BookCreate.as_view(), name='create_book'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('my_view', views.my_view, name='my_view'),
    path('profile/', views.CheckOutByUserView.as_view(), name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup')   # we are instatiating objects of class based views
]