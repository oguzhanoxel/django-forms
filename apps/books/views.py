from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

@login_required
def create(request):
    # Create Book
    form = BookCreateForm()
    if request.method == 'POST':
        if 'create_book' in request.POST:
            form = BookCreateForm(request.POST, request.FILES) # image eklenir ise (request.POST, request.FILES) olarak değiştilecek
            if form.is_valid():
                book = form.save(commit=False)
                book.created_by = request.user
                book.save()
                return redirect('index')
    else:
        form = BookCreateForm()
    ###

    # Create Category
    category_form = CategoryCreateForm()
    if request.method == 'POST':
        if 'create_category' in request.POST:
            if (request.user.is_admin == False):
                url = request.META.get('HTTP_REFERER')
                messages.warning(request, 'Only admin create category !')
                return redirect(url)
            else:
                url = request.META.get('HTTP_REFERER')
                category_form = CategoryCreateForm(request.POST) # image eklenir ise (request.POST, request.FILES) olarak değiştilecek
                if category_form.is_valid():
                    category_form.save()
                    return redirect(url)
    else:
        category_form = CategoryCreateForm()
    ###

    # Delete Category
    delete_category_form = CategoryDeleteForm()
    if request.method == 'POST':
        if 'delete_category' in request.POST:
            if (request.user.is_admin == False):
                url = request.META.get('HTTP_REFERER')
                messages.warning(request, 'Only admin delete category !')
                return redirect(url)
            else:
                url = request.META.get('HTTP_REFERER')
                delete_category_form = CategoryDeleteForm(request.POST)
                if delete_category_form.is_valid():
                    category = Category.objects.get(id = request.POST.get("category") )
                    category.delete()
                    return redirect(url)
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

@login_required
def update(request, id):
    # Update Book
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        print("ERROR: Book.DoesNotExist")
    if (request.user != book.created_by) and (request.user.is_admin == False):
        messages.warning(request, 'This book created by {}'.format(book.created_by.username))
        return redirect('detail', book.id)
    else:
        form = BookCreateForm(request.POST or None, request.FILES or None, instance=book)
        if 'create_book' in request.POST:
            if form.is_valid():
                form.save()
                return redirect('index')

  # Create Category
    category_form = CategoryCreateForm()
    if request.method == 'POST':
        if 'create_category' in request.POST:
            if (request.user.is_admin == False):
                url = request.META.get('HTTP_REFERER')
                messages.warning(request, 'Only admin create category !')
                return redirect(url)
            else:
                url = request.META.get('HTTP_REFERER')
                category_form = CategoryCreateForm(request.POST) # image eklenir ise (request.POST, request.FILES) olarak değiştilecek
                if category_form.is_valid():
                    category_form.save()
                    return redirect(url)
    else:
        category_form = CategoryCreateForm()
    ###

    # Delete Category
    delete_category_form = CategoryDeleteForm()
    if request.method == 'POST':
        if 'delete_category' in request.POST:
            if (request.user.is_admin == False):
                url = request.META.get('HTTP_REFERER')
                messages.warning(request, 'Only admin delete category !')
                return redirect(url)
            else:
                url = request.META.get('HTTP_REFERER')
                delete_category_form = CategoryDeleteForm(request.POST)
                if delete_category_form.is_valid():
                    category = Category.objects.get(id = request.POST.get("category") )
                    category.delete()
                    return redirect(url)
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

@login_required
def delete(request, id):
    book = Book.objects.get(id=id)

    if (request.user != book.created_by) and (request.user.is_admin == False):
        messages.warning(request, 'This book created by {}'.format(book.created_by.username))
        return redirect('detail', book.id)
    else:
        context = {
            'book': book,
        }
        template = 'books/delete_confirmation.html'
        return render(request, template, context)

@login_required
def delete_confirmation(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        print("ERROR: Book.DoesNotExist")
    if (request.user != book.created_by) and (request.user.is_admin == False):
        messages.warning(request, 'This book created by {}'.format(book.created_by.username))
        return redirect('detail', book.id)
    else:
        if request.method == 'POST':
            if book.image:
                book.image.delete()
            book.delete()
            return redirect('index')


