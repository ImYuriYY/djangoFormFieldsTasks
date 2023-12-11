from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *



newslist = [
    {
        'title': 'Post 1',
        'text': 'Text text text',
        'imgURL':'images/image1.jpg',
    },
    {
        'title': 'Post 2',
        'text': 'Text text text',
        'imgURL':'images/image2.jpg',
    },
    {
        'title': 'Post 3',
        'text': 'Text text text',
        'imgURL':'images/image3.jpg',
    },
    {
        'title': 'Post 4',
        'text': 'Text text text',
        'imgURL':'images/image1.jpg',
    },
    {
        'title': 'Post 5',
        'text': 'Text text text',
        'imgURL':'images/image2.jpg',
    },
    {
        'title': 'Post 6',
        'text': 'Text text text',
        'imgURL':'images/image3.jpg',
    },
    {
        'title': 'Post 7',
        'text': 'Text text text',
        'imgURL':'images/image1.jpg',
    },
    {
        'title': 'Post 8',
        'text': 'Text text text',
        'imgURL':'images/image2.jpg',
    },
    {
        'title': 'Post 9',
        'text': 'Text text text',
        'imgURL':'images/image3.jpg',
    },
]



def index(request):
    return render(request, 'news/index.html', context={'newslist': newslist})


def add(request):
    if request.method == 'POST':
        newslist.append(
            {
                'title': request.POST.get('title'),
                'text': request.POST.get('content'),
                'imgURL': ('images/' + request.POST.get('imag'))
            }
        )
        return HttpResponseRedirect('/news')
    newPostForm = NewPost()
    return render(request, 'news/addNews.html', context={'newPostForm': newPostForm})




