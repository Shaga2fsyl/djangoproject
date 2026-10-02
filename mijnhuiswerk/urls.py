from django.contrib import admin
from django.urls import include, path
from spelers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', views.post_list, name='post_list'),
]