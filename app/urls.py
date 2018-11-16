from django.urls import path

from . import views

urlpatterns = [
    path('engage', views.start_process, name='engage'),
    path('step/<int:server_id>/<int:step>/', views.get_result, name='get-step'),
]
