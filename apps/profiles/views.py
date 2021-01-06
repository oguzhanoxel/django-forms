from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ReadingPageForm

from .models import Wishlist, FinishedList, ReadingList
from apps.users.models import User
from apps.books.models import Book

@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'user': user,
    }
    template = 'users/profile.html'
    return render(request, template, context)

@login_required
def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist': wishlist,
        'is_wishlist': True,
    }
    template = 'users/lists/wishlist.html'
    return render(request, template, context)

@login_required
def add_wishlist(request, id):
    book = Book.objects.get(id=id)

    wished_book = Wishlist.objects.get_or_create(user=request.user, book=book)

    return redirect('wishlist')

@login_required
def remove_wishlist(request, id):
    wishlist = Wishlist.objects.filter(user=request.user)
    book = Book.objects.get(id=id)
    for wished_book in wishlist:
        if wished_book.book == book:
            wished_book.delete()
    
    return redirect('wishlist')

@login_required
def finishedlist(request):
    finishedlist = FinishedList.objects.filter(user=request.user)
    context = {
        'finishedlist': finishedlist,
        'is_finishedlist': True,
    }
    template = 'users/lists/finishedlist.html'
    return render(request, template, context)

@login_required
def add_finishedlist(request, id):
    book = Book.objects.get(id=id)

    finished_book = FinishedList.objects.get_or_create(user=request.user, book=book, is_finished=True)

    return redirect('finishedlist')

@login_required
def remove_finishedlist(request, id):
    finishedlist = FinishedList.objects.filter(user=request.user)
    book = Book.objects.get(id=id)
    for finished_book in finishedlist:
        if finished_book.book == book:
            finished_book.delete()
    
    return redirect('finishedlist')

@login_required
def readinglist(request):
    readinglist = ReadingList.objects.filter(user=request.user)
    context = {
        'readinglist': readinglist,
        'is_readinglist': True,
    }
    template = 'users/lists/readinglist.html'
    return render(request, template, context)

@login_required
def add_readinglist(request, id):
    book = Book.objects.get(id=id)

    reading_book = ReadingList.objects.get_or_create(user=request.user, book=book)

    return redirect('readinglist')

@login_required
def remove_readinglist(request, id):
    readinglist = ReadingList.objects.filter(user=request.user)
    book = Book.objects.get(id=id)
    for reading_book in readinglist:
        if reading_book.book == book:
            reading_book.delete()
    
    return redirect('readinglist')
            

    