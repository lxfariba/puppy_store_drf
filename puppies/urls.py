from django.urls import path
from . import views



urlpatterns = [
    path(
        r'api/v1/puppies/(<int:pk>)$',
        views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    path(
        r'api/v1/puppies/$',
        views.get_post_puppies,
        name='get_post_puppies'
    )
]

