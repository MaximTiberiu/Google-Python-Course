from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('updateProfile/<int:pk>', views.UpdateProfileView.as_view(), name='modificare_profil'),
    path('new_account/', views.CreateNewUser.as_view(), name='adaugare_utilizator'),
]