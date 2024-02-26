from django.urls import path
from . import views

app_name = 'props'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:prop_id>', views.detail, name='detail')
]