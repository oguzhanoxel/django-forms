from django.shortcuts import render, redirect


from .models import Wishlist
from apps.users.models import User
from apps.books.models import Book

def profile(request, id):
    user = User.objects.get(id=id)
    wishlist = Wishlist.objects.filter(user=user)
    context = {
        'user': user,
        'wishlist': wishlist,
    }
    template = 'users/profile.html'
    return render(request, template, context)

def add_wishlist(request, id):
    book = Book.objects.get(id=id)

    wished_book = Wishlist.objects.get_or_create(user=request.user, book=book)

    return redirect('profile', id=request.user.id)

def remove_wishlist(request, id):
    wishlist = Wishlist.objects.filter(user=request.user)
    book = Book.objects.get(id=id)
    for wished_book in wishlist:
        if wished_book.book == book:
            wished_book.delete()
    
    return redirect('profile', id=request.user.id)


    