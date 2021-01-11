from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Book, Category, Comment
from .forms import (
    BookCreateForm,
    CategoryCreateForm,
    CategoryDeleteForm,
    CommentForm,
)    

def index(request):
    books = Book.objects.all()

    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'books': books,
    }
    template = 'books/index.html'
    return render(request, template, context)

def search(request):
    books = Book.objects.all()

    query = request.GET.get('q')

    if query:
        books = books.filter(
            Q(category__title__icontains=query) | Q(title__icontains=query) | Q(desc__icontains=query) | Q(author__icontains=query) | Q(created_by__username__icontains=query)
        ).distinct()

    context = {
        'books': books,
    }
    template = 'books/index.html'
    return render(request, template, context)

def detail(request, id):
    book = Book.objects.get(id=id)
    comments = Comment.objects.filter(book = book)

    form = CommentForm()
    if request.method == "POST":
        if 'send_comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment.objects.create(book=book, user=request.user)
                comment.text = form.cleaned_data['text']
                comment.save()
                form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'book': book,
        'form': form,
        'comments': comments,
    }
    template = 'books/detail.html'
    return render(request, template, context)

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id = id)
    if request.user == comment.user:
        comment.delete()

    return redirect('detail', comment.book.id)

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
        book = get_object_or_404(Book, id=id)
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
    book = get_object_or_404(Book, id=id)

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
        book = get_object_or_404(Book, id=id)
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
