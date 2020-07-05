from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models
from . import forms


def check_user_blog(request, blog):
    """Checks if the requested blog belongs to the
    requested user."""
    if request.user != blog.owner:
        raise Http404


def index(request):
    """Renders the home page."""
    return render(request, 'blogs/index.html')


def blogs(request):
    """Renders the blogs page."""
    blogs = models.Blog.objects.order_by('-date_added')
    return render(request, 'blogs/blogs.html', {'blogs': blogs})


@login_required
def my_blogs(request):
    """Renders the user blogs page"""
    blogs = models.Blog.objects.all()
    blogs = filter(lambda x: x.owner == request.user, blogs)
    return render(request, 'blogs/my_blogs.html', {'blogs': blogs})


@login_required
def blog(request, blog_id):
    """Renders the blog page."""
    blog = get_object_or_404(models.Blog, id=blog_id)
    comments = blog.comment_set.order_by('-date_added')
    return render(request, 'blogs/blog.html', {'blog': blog,
                                               'comments': comments})


@login_required
def new_blog(request):
    if request.method != 'POST':
        # No data submitted; Create a blank form
        form = forms.NewBlogForm()
    else:
        # Data submitted; process it
        form = forms.NewBlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')

    # Display the content or not
    return render(request, 'blogs/new_blog.html', {'form': form})


@login_required
def edit_blog(request, blog_id):
    """Blog edition session page."""
    blog = models.Blog.objects.get(id=blog_id)
    check_user_blog(request, blog)
    if request.method != 'POST':
        # No data submitted; Create a blank form
        form = forms.NewBlogForm(instance=blog)
    else:
        # Data submitted; Process it
        form = forms.NewBlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            edited_blog = form.save(commit=False)
            edited_blog.save()
            return redirect('blogs:blog', blog_id=blog_id)

    # Display the data or not
    return render(request, 'blogs/edit_blog.html', {'form': form,
                                                    'blog': blog})


@login_required
def new_comment(request, blog_id):
    """Renders the page for adding comments about a blog."""
    blog = get_object_or_404(models.Blog, id=blog_id)
    if request.method != 'POST':
        # Create a blank form
        form = forms.NewCommentForm()
    else:
        # Process the data
        form = forms.NewCommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.blog = blog
            new_comment.save()
            return redirect('blogs:blog', blog_id=blog_id)

    # Display the data or not
    return render(request, 'blogs/new_comment.html', {'form': form,
                                                      'blog': blog})
