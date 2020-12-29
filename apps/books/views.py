from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import (
    BookCreateForm,
    CategoryCreateForm,
    CategoryDeleteForm,
)    

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
    # Create Book
    form = BookCreateForm()
    if request.method == 'POST':
        if 'create_book' in request.POST:
            form = BookCreateForm(request.POST, request.FILES) # image eklenir ise (request.POST, request.FILES) olarak değiştilecek
            if form.is_valid():
                form.save()
                return redirect('index')
    else:
        form = BookCreateForm()
    ###

    # Create Category
    category_form = CategoryCreateForm()
    if request.method == 'POST':
        if 'create_category' in request.POST:
            category_form = CategoryCreateForm(request.POST) # image eklenir ise (request.POST, request.FILES) olarak değiştilecek
            if category_form.is_valid():
                category_form.save()
                return redirect('create')
    else:
        category_form = CategoryCreateForm()
    ###

    # Delete Category
    delete_category_form = CategoryDeleteForm()
    if request.method == 'POST':
        if 'delete_category' in request.POST:
            delete_category_form = CategoryDeleteForm(request.POST)
            if delete_category_form.is_valid():
                category = Category.objects.get(id = request.POST.get("category") )
                category.delete()
                return redirect('create')
    else:
        delete_category_form = CategoryDeleteForm()
    ###

    context = {
        'form': form,
        'category_form': category_form,
        'delete_category_form': delete_category_form,
        'is_create': True,
    }
    template = 'books/edit.html'
    return render(request, template, context)

def update(request, id):
    # Update Book
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        print("ERROR: Book.DoesNotExist")
    form = BookCreateForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')

    # Create Category
    category_form = CategoryCreateForm()
    if request.method == 'POST':
        if 'create_category' in request.POST:
            category_form = CategoryCreateForm(request.POST) # image eklenir ise (request.POST, request.FILES) olarak değiştilecek
            if category_form.is_valid():
                category_form.save()
                return redirect('create')
    else:
        category_form = CategoryCreateForm()
    ###

    # Delete Category
    delete_category_form = CategoryDeleteForm()
    if request.method == 'POST':
        if 'delete_category' in request.POST:
            delete_category_form = CategoryDeleteForm(request.POST)
            if delete_category_form.is_valid():
                category = Category.objects.get(id = request.POST.get("category") )
                category.delete()
                return redirect('create')
    else:
        delete_category_form = CategoryDeleteForm()
    ###
    
    context = {
        'form': form,
        'category_form': category_form,
        'delete_category_form': delete_category_form,
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
        if book.image:
            book.image.delete()
        book.delete()
        return redirect('index')


