from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
    path('remove_wishlist/<int:id>', views.remove_wishlist, name='remove_wishlist'),
    path('<int:id>', views.profile, name='profile'),
]