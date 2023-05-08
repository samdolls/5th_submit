from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('information/', information, name="information"),
    path('notion/', notion, name="notion"),
    path('talking/', talking, name="talking"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]