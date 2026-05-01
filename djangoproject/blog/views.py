from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':"blog",
        'subtitle':"Ini adalah Halaman Blog ",
        # 'nav':[
        #     ['/',"Home"],
        #     ['/blog',"Blog"],
        #     ['/kontak',"Kontak"],
        #
        # ],
        'banner': 'images/about.png'
    }
    # return render(request,'blog/index.html',context)
    return render(request,'index.html',context)
