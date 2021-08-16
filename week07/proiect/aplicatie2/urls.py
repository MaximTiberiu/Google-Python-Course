from django.urls import path
from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns = [
    path('adaugare/', views.CreateCompaniesView.as_view(), name='adaugare'),
    path('modificare/<int:pk>', views.UpdateCompaniesView.as_view(), name='modifica'),
    path('list/', views.ListCompaniesView.as_view(), name='listare'),
]