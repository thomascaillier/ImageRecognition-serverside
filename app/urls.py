from django.urls import path

from . import views

urlpatterns = [
    path('img_searches', views.post_image , name='post_image'),
    path('img_searches/<int:server_id>', views.get_data, name='get_data'),
]
