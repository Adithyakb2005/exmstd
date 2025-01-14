from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.list_contacts, name='list_contacts'),  
    path('contacts/', RedirectView.as_view(url='/', permanent=False)), 
    path('add/', views.add_contact, name='add_contact'),
    path('<int:pk>/', views.view_contact, name='default_view_contact'),
    path('<int:id>/edit/', views.edit_contact, name='edit_contact'),
    path('<int:pk>/delete/', views.delete_contact, name='delete_contact'),
    path('<int:pk>/call/', views.call_contact, name='call_contact'),
]
