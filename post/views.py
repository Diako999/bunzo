from django.shortcuts import redirect
from django.shortcuts import render
from .models import Post
from django.contrib import messages
def posts(request):
    pass


def write_post(request):
    return render(request, 'write-post.html')

def publish_post(request):
    posts = Post.objects.all()
    if request.method == "POST":
        tag = request.POST['tag']
        title = request.POST['title']
        description = request.POST['description']
        print(request.user)
        if tag == "" or title =="" or description == "":
            messages.error(request, 'you must fill all the fields')
            return redirect('write_post')
        new_post = posts.create(author = request.user, title = title, post_detail = description , tag = tag)
        new_post.save()
        messages.success(request, 'post added successfully!!')
        return redirect('index')


    return redirect('index')

def post_detail(request, id):
    post = Post.objects.get(id = id)
    context = {
    'post' : post
    }
    return render(request, 'post_detail.html', context)
