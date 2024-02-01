from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('ross/', views.ross, name='ross'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),

]