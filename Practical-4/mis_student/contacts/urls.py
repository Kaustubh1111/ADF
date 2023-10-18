from django.urls import path
from .views import *

urlpatterns = [
    path('',ContactList.as_view(), name='contact_list'),
    path('<int:pk>/',ContactDetail.as_view(), name='contact_detail'),
    path('<int:pk>/update/',ContactUpdate.as_view(), name='contact_update'),
    path('<int:pk>/delete/',ContactDelete.as_view(), name='contact_delete'),
    path('create/',ContactCreate.as_view(), name='contact_create'),
]
