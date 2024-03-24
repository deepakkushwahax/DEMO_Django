from django.urls import path
from exam import views
urlpatterns = [
    path('Testpaper',views.testpaper),
    path('Result',views.result)
]
