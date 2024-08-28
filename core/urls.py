from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather_view'),
    # path('generate-blog/', views.generate_blog, name='generate_blog')
]