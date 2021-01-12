from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>', views.category, name='category'),
    path('search', views.search, name='search'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('delete_comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete/<int:id>/delete-confirmation', views.delete_confirmation, name='delete_confirmation'),
]