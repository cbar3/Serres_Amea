from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Image


def post_list(request):
    cat = request.GET.get('cat', '')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False
    if cat is False:
        if txt == '':
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date',)
        else:
            posts = Post.objects.filter(published_date__lte=timezone.now()).filter(text__contains=txt).order_by(
                '-published_date')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('-published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    imageList = Image.objects.filter(postID=pk)
    context = {
        'post': post,
        'imageList': imageList,
    }
    return render(request, 'blog/post_detail.html', context, )


def aboutus(request):
    return render(request, 'blog/aboutus.html')


def history(request):
    return render(request, 'blog/istoria.html')


def announcement(request):
    cat = request.GET.get('cat', '1')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False
    if cat is False:
        if txt == '':
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        else:
            posts = Post.objects.filter(published_date__lte=timezone.now()).filter(text__contains=txt).order_by(
                '-published_date')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('-published_date')

    return render(request, 'blog/announcement.html', {'posts': posts})


def deltia(request):
    cat = request.GET.get('cat', '2')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False
    if cat is False:
        if txt == '':
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        else:
            posts = Post.objects.filter(published_date__lte=timezone.now()).filter(text__contains=txt).order_by(
                '-published_date')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('-published_date')

    return render(request, 'blog/deltia_typou.html', {'posts': posts})


def image_list(request):
    post = Image.objects.filter(active=1,)
    return render(request, 'blog/ergastirio.html', {'post': post}, )
