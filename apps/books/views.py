from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreateForm


def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    template = 'books/index.html'
    return render(request, template, context)

def detail(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
    }
    template = 'books/detail.html'
    return render(request, template, context)

def create(request):
    form = BookCreateForm()
    if request.method == 'POST':
        form = BookCreateForm(request.POST) # image eklenir ise (request.POST, request.FILES) olarak değiştilecek
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookCreateForm()
    context = {
        'form': form,
        'is_create': True,
    }
    template = 'books/edit.html'
    return render(request, template, context)

def update(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        print("ERROR: Book.DoesNotExist")
    form = BookCreateForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
        'book': book,
        'is_update':True,
    }
    template = 'books/edit.html'
    return render(request, template, context)

def delete(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
    }
    template = 'books/delete_confirmation.html'
    return render(request, template, context)


def delete_confirmation(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        print("ERROR: Book.DoesNotExist")
    if request.method == 'POST':
        book.delete()
        return redirect('index')

