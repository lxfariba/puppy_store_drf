from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', include('puppies.urls')),
    path(
        r'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path('admin/', admin.site.urls),
]

