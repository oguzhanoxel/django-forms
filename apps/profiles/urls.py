from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('myprofile/', views.myprofile, name='myprofile'),
    path('profile/<int:id>', views.otherprofile, name='otherprofile'),

    path('wishlist/<int:id>', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
    path('remove_wishlist/<int:id>', views.remove_wishlist, name='remove_wishlist'),

    path('readinglist/<int:id>', views.readinglist, name='readinglist'),
    path('add_readinglist/<int:id>', views.add_readinglist, name='add_readinglist'),
    path('remove_readinglist/<int:id>', views.remove_readinglist, name='remove_readinglist'),

    path('finishedlist/<int:id>', views.finishedlist, name='finishedlist'),
    path('add_finishedlist/<int:id>', views.add_finishedlist, name='add_finishedlist'),
    path('remove_finishedlist/<int:id>', views.remove_finishedlist, name='remove_finishedlist'),

]