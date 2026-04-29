from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':"blog",
        'developer':"Pargoy",
        'nav':[
            ['/',"Home"],
            ['/blog',"Blog"],
            ['/blog/artikel',"Artikel"],
            ['/blog/berita',"Berita"],
        ]
    }
    return render(request,'blog/index.html',context)
