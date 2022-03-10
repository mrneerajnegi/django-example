from django.urls import path
from user import views
app_name="user"
urlpatterns=[
    path('login/',views.user_login,name="login"),
    path('register/', views.registration,name="register"),
    path('logout_user/', views.logout_user, name="logout"),

]