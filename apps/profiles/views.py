from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PageUpdateForm

from .models import List
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
    user = request.user
    wishlist = List.objects.filter(user=user, is_wished=True)
    context = {
        'wishlist': wishlist,
    }
    template = 'users/lists/wishlist.html'
    return render(request, template, context)

@login_required
def add_wishlist(request, id):
    user = request.user
    book = Book.objects.get(id = id)
    
    List.objects.get_or_create(user=user, book=book)

    wishbook = List.objects.get(user=user, book=book)
    wishbook.is_wished = True
    wishbook.is_finished = False
    wishbook.is_reading = False
    wishbook.save()
    messages.success(request, '{} has been added wishlist'.format(wishbook.book.title))
    return redirect('wishlist')

@login_required
def remove_wishlist(request, id):
    user = request.user
    book = Book.objects.get(id=id)
    wished_book = List.objects.get(user=user, book=book, is_wished=True)
    wished_book.is_wished = False
    wished_book.save()
    return redirect('wishlist')

@login_required
def readinglist(request):
    user = request.user
    readinglist = List.objects.filter(user=user, is_reading=True)

    page_update_form = PageUpdateForm()
    if request.method == "POST":
        for reading_book in readinglist:
            if str(reading_book.id) in request.POST:
                page_update_form = PageUpdateForm(request.POST)
                print(page_update_form)
                if page_update_form.is_valid():
                    reading_book = List.objects.get(id = reading_book.id)
                    reading_book.last_page = page_update_form.cleaned_data['last_page']
                    reading_book.save()
                    return redirect('readinglist')
    else:
        page_update_form = PageUpdateForm()

    context = {
        'page_update_form': page_update_form,
        'readinglist': readinglist,
    }
    template = 'users/lists/readinglist.html'
    return render(request, template, context)

@login_required
def add_readinglist(request, id):
    user = request.user
    book = Book.objects.get(id = id)

    List.objects.get_or_create(user=user, book=book)

    readingbook = List.objects.get(user=user, book=book)
    readingbook.is_wished = False
    readingbook.is_finished = False
    readingbook.is_reading = True
    readingbook.save()

    messages.success(request, '{} has been added reading list'.format(readingbook.book.title))

    return redirect('readinglist')

@login_required
def remove_readinglist(request, id):
    user = request.user
    book = Book.objects.get(id=id)
    readingbook = List.objects.get(user=user, book=book, is_reading=True)
    readingbook.is_reading = False
    readingbook.save()
    return redirect('readinglist')

@login_required
def finishedlist(request):
    user = request.user
    finishedlist = List.objects.filter(user=user, is_finished=True)
    context = {
        'finishedlist': finishedlist,
    }
    template = 'users/lists/finishedlist.html'
    return render(request, template, context)

@login_required
def add_finishedlist(request, id):
    user = request.user
    book = Book.objects.get(id = id)

    List.objects.get_or_create(user=user, book=book)

    finishedbook = List.objects.get(user=user, book=book)
    finishedbook.is_wished = False
    finishedbook.is_finished = True
    finishedbook.is_reading = False
    finishedbook.save()

    messages.success(request, '{} has been added finished list'.format(finishedbook.book.title))

    return redirect('finishedlist')

@login_required
def remove_finishedlist(request, id):
    user = request.user
    book = Book.objects.get(id=id)
    finishedbook = List.objects.get(user=user, book=book, is_finished=True)
    finishedbook.is_finished = False
    finishedbook.save()
    return redirect('finishedlist')
    