from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('home/', views.HomeView.as_view(), name="home"),
    path('', LoginView.as_view(template_name="app/login.html", next_page='home'), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('profile/<str:username>/<int:pk>/', views.ProfileView.as_view(), name="profile")
]
