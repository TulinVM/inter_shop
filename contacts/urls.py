#contacts/urls.py
from django.urls import path
from . import views
from .views import ContactView, ContactView1

app_name = 'contacts'

urlpatterns = [
    path("", ContactView.as_view(), name="contacts"),
    path('contacts/tel', ContactView1.as_view(), name='tel'),
    path('contacts/tel_copy', ContactView.as_view(), name='tel_copy'),
]
