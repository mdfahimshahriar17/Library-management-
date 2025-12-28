from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import BlogFrom
from django.contrib.auth.decorators import login_required



def blog_list(request):
    blogs = Post.objects.all().order_by('-created_at')

    return render(request, 'blog/blog_list.html', {'blogs': blogs})


@login_required
def create_blog(request):

    if request.method == 'POST':
        form = BlogFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        
    else:
        form = BlogFrom()
    return render(request, 'blog/create_blog.html', {'form': form})



@login_required
def edit_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = BlogFrom(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        
    else:
        form = BlogFrom(instance=post)

    return render(request, 'blog/edit_blog.html', {'form': form})



@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    blog.delete()

    return redirect('blog_list')


