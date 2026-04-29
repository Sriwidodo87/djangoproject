from django.shortcuts import render
def index(request):
    context = {
        'title':"My Website",
        "developer":"Sri Widodo",
    }
    return render(request, 'index.html',context)